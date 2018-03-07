from django.http import HttpResponse
from django.http import JsonResponse
import re
import json
import pandas as pd
from pandas.io.json import json_normalize
from textblob import TextBlob
# import matplotlib.pyplot as plt

def analyse(request):
    query_string=request.GET['file']
    tweets_data_path = 'capstone/raw_data/'+query_string + '.txt'
    tweets_data = []
    tweets_file = open(tweets_data_path, "r")
    processedFile = open("processed","w+")
    # print(tweets_file)
    for line in tweets_file:
        try:
            tweet = json.loads(line)
            tweets_data.append(tweet)
        except:
            continue

    print len(tweets_data)
    print(type(tweets_data)) ;
    tweets = pd.DataFrame()
    # print(tweets_data)
    # b = json.loads(a) ;

    tables = json_normalize(tweets_data)
    # processedFile.write(tables)
    # print(tables)
    tweets['text'] = map(lambda tweet: tweet['text'], tweets_data)
    tweets['lang'] = map(lambda tweet: tweet['lang'], tweets_data)
    tweets['country'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)

    # print(tweets['text'])

    sentimentalTweets = []

    for tweet in tweets['text']:
        # empty dictionary to store required params of a tweet
        parsed_tweet = {}

        # saving text of tweet
        parsed_tweet['text'] = tweet
        # saving sentiment of tweet
        parsed_tweet['sentiment'] = get_tweet_sentiment(tweet)

        sentimentalTweets.append(parsed_tweet)

    # print(sentimentalTweets)

    # picking positive tweets from tweets
    ptweets = [tweet for tweet in sentimentalTweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    positivePercentage = 100*len(ptweets)/len(tweets) ;
    print("Positive tweets percentage: {} %".format(100*len(ptweets)/len(sentimentalTweets)))
    # picking negative tweets from tweets
    ntweets = [tweet for tweet in sentimentalTweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    negativePercentage = 100*len(ntweets)/len(tweets) ;
    print("Negative tweets percentage: {} %".format(100*len(ntweets)/len(sentimentalTweets)))
    
    #get neutral tweets
    neutralTweets = [tweet for tweet in sentimentalTweets if tweet['sentiment'] == 'neutral']
    # percentage of neutral tweets
    neutralPercentage = 100*(len(tweets) - len(ntweets) - len(ptweets))/len(tweets) ;
    print("Neutral tweets percentage: {} % ".format(100*(len(sentimentalTweets) - len(ntweets) - len(ptweets))/len(sentimentalTweets)))

    # printing first 5 positive tweets
    # print("\n\nPositive tweets:")
    # for tweet in ptweets[:10]:
    #     print(tweet['text'])

    totalTweets = len(sentimentalTweets) ;
    return JsonResponse({
        "positivePercentage" : positivePercentage ,
        "negativePercentage" : negativePercentage ,
        "neutralPercentage" : neutralPercentage ,
        "total":totalTweets,
        "positive" : ptweets,
        "negative": ntweets,
        "neutral" : neutralTweets})

def clean_tweet(tweet):
    '''
    Utility function to clean tweet text by removing links, special characters
    using simple regex statements.
    '''
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

def get_tweet_sentiment(tweet):
    '''
    Utility function to classify sentiment of passed tweet
    using textblob's sentiment method
    '''
    # create TextBlob object of passed tweet text
    analysis = TextBlob(clean_tweet(tweet))
    # set sentiment
    # print(analysis.sentiment.polarity)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'





# print(tweets_data)

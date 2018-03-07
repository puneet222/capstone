from django.http import HttpResponse
from django.http import JsonResponse

def instantAnalysis(request):
    query_string=request.GET['query']

    return main(query_string)
    #return HttpResponse("Hello, world. You're at the polls index.")
    #return JsonResponse({'foo':'bar'})



import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'blivRaci1wkPVJTEcn9WTMZI1'
        consumer_secret = 'AwFx2fDHt75bCNmQAmVHoz2eC0JK7vpG8dsdTt7qFcD4YJno3q'
        access_token = '3263374020-pYo8R6Soj9CqW0IMFvnEL7PHbhhw3332hYQiEUK'
        access_token_secret = 'bPEOpR83lW1KCZ1dhYs6B0rGNtCrKA85rdLkmzvIgeYdS'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        print(analysis.sentiment.polarity)
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))

def main(query_url):
    # creating object of TwitterClient Class
    api = TwitterClient()
    # Get the input from user
    #sentiment_query = raw_input("Enter the keyword ")
    #print ("your sentiment query is : " , sentiment_query)
    # calling function to get tweets
    tweets = api.get_tweets(query =query_url , count = 500)

    # picking positive tweets from tweets
    postiveTweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
    # percentage of positive tweets
    positivePercentage = 100*len(postiveTweets)/len(tweets) ;
    print("Positive tweets percentage: {} %".format(100*len(postiveTweets)/len(tweets)))
    # picking negative tweets from tweets
    negativeTweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
    # percentage of negative tweets
    negativePercentage = 100*len(negativeTweets)/len(tweets) ;
    print("Negative tweets percentage: {} %".format(100*len(negativeTweets)/len(tweets)))

    #get neutral tweets
    neutralTweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']
    # percentage of neutral tweets
    neutralPercentage = 100*(len(tweets) - len(negativeTweets) - len(postiveTweets))/len(tweets) ;
    print("Neutral tweets percentage: {} % ".format(100*(len(tweets) - len(negativeTweets) - len(postiveTweets))/len(tweets)))



    print("Total Tweets : ")
    print(len(tweets)) ;

    return JsonResponse({"positivePercentage" : positivePercentage ,
    "negativePercentage" : negativePercentage ,
    "neutralPercentage" : neutralPercentage ,
    "positive":postiveTweets,
    "negative":negativeTweets,
    "neutral":neutralTweets})

    # --------------------------------------------------------------------------------------------------------------------

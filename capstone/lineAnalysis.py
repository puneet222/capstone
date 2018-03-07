from django.http import HttpResponse
from django.http import JsonResponse
from textblob import TextBlob

def lineAnalysis(request):
    query_string=request.GET['query']
    return analyse(query_string)


def get_sentiment(analysis):

	if analysis.sentiment.polarity > 0:
		return 'positive'
	elif analysis.sentiment.polarity == 0:
		return 'neutral'
	else:
		return 'negative'

def analyse(string):
	
	analysis = TextBlob(string)

	return JsonResponse({
		"line" : string,
		"sentiment" : get_sentiment(analysis),
		"polarity" : analysis.sentiment.polarity
		})

from django.http import HttpResponse
from django.http import JsonResponse

def dataGen(request):
    query_string=request.GET['file']
    # filename = query_string + ".txt"
    # print(filename)
    # consumer_key = 'blivRaci1wkPVJTEcn9WTMZI1'
    # consumer_secret = 'AwFx2fDHt75bCNmQAmVHoz2eC0JK7vpG8dsdTt7qFcD4YJno3q'
    # access_token = '3263374020-pYo8R6Soj9CqW0IMFvnEL7PHbhhw3332hYQiEUK'
    # access_token_secret = 'bPEOpR83lW1KCZ1dhYs6B0rGNtCrKA85rdLkmzvIgeYdS'
    #
    # #This handles Twitter authetification and the connection to Twitter Streaming API
    # l = StdOutListener()
    # l.openFile(filename)
    # auth = OAuthHandler(consumer_key, consumer_secret)
    # auth.set_access_token(access_token, access_token_secret)
    # stream = Stream(auth, l)
    # #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    # stream.filter(track=['politics' , 'narendra modi' , 'bjp'])






#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
# import matplotlib.pyplot as plt

# print ("okay") ;

#Variables that contains the user credentials to access Twitter API
# access_token = "3263374020-pYo8R6Soj9CqW0IMFvnEL7PHbhhw3332hYQiEUK"
# access_token_secret = "bPEOpR83lW1KCZ1dhYs6B0rGNtCrKA85rdLkmzvIgeYdS"
# consumer_key = "h4Yfsr2W6xDRK3uu5O4apjZK0"
# consumer_secret = "NUWDsCK6ahaAdWPn3CNPjdCbJqNqgtDkMQEh8hc0LicIgVF4B0"


# count = 0 ;
# dataFile = open(fileurl,"w+")
# stringFile=""
#
# def incrementCount():
#     print("haha")
#
# #This is a basic listener that just prints received tweets to stdout.
# class StdOutListener(StreamListener):
#
#
#
#
#     # tweets = []
#
#     def on_data(self, data):
#         # tweets.append(data) ;
#         # incrementCount() ;
#         stringFile=stringFile + "\n" + data;
#         print (data)
#         return True
#
#     def on_error(self, status):
#         print ("status is : ")
#         print(status)

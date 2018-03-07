#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import pandas as pd
import sys
import os




count = 0 ;



def initStreamingApi(file , filterArr):
    consumer_key = 'blivRaci1wkPVJTEcn9WTMZI1'
    consumer_secret = 'AwFx2fDHt75bCNmQAmVHoz2eC0JK7vpG8dsdTt7qFcD4YJno3q'
    access_token = '3263374020-pYo8R6Soj9CqW0IMFvnEL7PHbhhw3332hYQiEUK'
    access_token_secret = 'bPEOpR83lW1KCZ1dhYs6B0rGNtCrKA85rdLkmzvIgeYdS'

    #This handles Twitter authetification and the connection to Twitter Streaming API
    listener = StdOutListener(file)
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)
    stream.filter(track=filterArr)



#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def __init__(self , file):
        self.file = file;
        self.count = 0;

    def on_data(self, data):    
        self.count = self.count + 1;
        print('count -> {}'.format(self.count));
        self.file.write(data);
        return True;

    def on_error(self, status):
        print ("status is : ")
        print(status)





filename = sys.argv[1];
print('Using file name '+filename+'.txt');
filePath = 'raw_data/'+filename+'.txt';
filters = sys.argv[2:];
print('using filters as ->');
print(filters);
print('------------------STARTING-------------------------------')

# if(os.path.exists(filePath)):
#     print('file exists provide another filename');
# else:
print('new file');
file = open(filePath,'a+');
filterArr = filters;
initStreamingApi(file , filterArr);



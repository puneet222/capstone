var fs = require('fs');

var parsedTweets = fs.readFileSync('./analysedSample.txt' , 'utf8');


var singleTweets = parsedTweets.split('\n');
var parsedString = '';
var parsedCSV = '';


function  getNormalisedSentiment(sentiment) {
	if(sentiment=='positive'){
		return 'positive';
	}else if(sentiment == 'negative'){
		return 'negative';
	}else{
		return 'neutral';
	}
}
singleTweets.forEach(function(tweet){
	var tweetFields = tweet.split('\t');
	var result = {
		tweet : tweetFields[3],
		sentiment : getNormalisedSentiment(tweetFields[2])
	}
	parsedString = parsedString +  JSON.stringify(result) + '\n';
	parsedCSV = parsedCSV + tweetFields[3] +','+ getNormalisedSentiment(tweetFields[2]) + '\n';
});


fs.writeFileSync('./parsedSample.csv', parsedCSV , 'utf8');
fs.writeFileSync('./parsedSampleResults.txt' , parsedString , 'utf8');
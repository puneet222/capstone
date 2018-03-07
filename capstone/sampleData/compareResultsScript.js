var fs = require('fs');

var sampleResults = fs.readFileSync('./parsedSampleResults.txt' , 'utf8');
var calculatedResults = fs.readFileSync('./calculatedResults.txt' , 'utf8');

var sampleResultsArray = sampleResults.split('\n');
var calculatedResultsArray = calculatedResults.split('\n');

console.log('========starting comparision=======');

var samplePositiveCount=0;
var sampleNegativeCount=0;
var sampleNeutralCount=0;
var calculatedPositiveCount=0;
var calculatedNegativeCount=0;
var calculatedNeutralCount=0;

var accurray = 0;
var total = sampleResultsArray.length;

var finalResultsCSV = 'tweet\tsampleResult\tcalculatedResults\n';

sampleResultsArray.forEach(function(sampleTweetResultStr , index ){
	if(!sampleTweetResultStr){
		return;
	}
	var sampleTweetResult = JSON.parse(sampleTweetResultStr);
	var calculatedTweetResult = JSON.parse(calculatedResultsArray[index]);

	//console.log('s ->' + sampleTweetResult.sentiment +' | c-> '+calculatedTweetResult.sentiment );
	
	if(sampleTweetResult.sentiment==calculatedTweetResult.sentiment){
		accurray ++;
	}

	if(sampleTweetResult.sentiment=='positive'){
		samplePositiveCount++;
	}else if(sampleTweetResult.sentiment=='negative'){
		sampleNegativeCount++;
	}else if(sampleTweetResult.sentiment=='neutral'){
		sampleNeutralCount++;
	}

	if(calculatedTweetResult.sentiment=='positive'){
		calculatedPositiveCount++;
	}else if(calculatedTweetResult.sentiment=='negative'){
		calculatedNegativeCount++;
	}else if(calculatedTweetResult.sentiment=='neutral'){
		calculatedNeutralCount++;
	}



	finalResultsCSV = finalResultsCSV + sampleTweetResult.tweet +'\t'+ sampleTweetResult.sentiment +'\t'+ calculatedTweetResult.sentiment + '\n';


});


fs.writeFileSync('results.tsv' , finalResultsCSV , 'utf8');

console.log('------------results----------------');
console.log('total ->'+total);
console.log('accurray -> '+accurray);
console.log('----sample results-----');
console.log('positive -> '+samplePositiveCount);
console.log('negative -> '+sampleNegativeCount);
console.log('neutral -> '+sampleNeutralCount);

console.log('----calculated results-----');
console.log('positive -> '+calculatedPositiveCount);
console.log('negative -> '+calculatedNegativeCount);
console.log('neutral -> '+calculatedNeutralCount);
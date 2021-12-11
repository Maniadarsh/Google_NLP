# Working with Google_NLP and Twitter API 
First a simple python code was done to understand the working of google cloud natural language processing API.
A text was given as input to two functions
One function did sentiment analysis and the other did entity analysis.
A google cloud account was created after which API's were enabled and service accounts were created.
The key of the service account is important for the program to work which is a json file downloaded to your computer.
Language module was imported from google cloud.
Name,type and salience were analysed in entity analysis.
source: https://codelabs.developers.google.com/codelabs/cloud-natural-language-python3#6


Then a simple code was done to understand the working of twitter API. The program took a keyword and outputs all the tweets related to the keyword. Document
Specific modules such as tweepy were imported for that. The output for twitter API can be seen in the wiki page.

USER STORIES:
Find negative and positive trends. 

Trends imply that for a new product released in the market, product owners can see how well is the reception for their product, this is one of the many use cases. 

USERS:
Analysts,
Business owners

MVP:
A product that takes a keyword and does sentiment analysis on the tweets that contain the keyword.

2 programs were executed one with a positive keyword and another with a negative keyword. Twitter and google cloud modules required for running the API were imported. 5 modules were defined. 

First module for authenticating Twitter API. Second module for retrieving tweets from twitter according to the keyword and count.
Third module for cleaning the tweets i.e removing hyoerlinks, special characters etc.
Fourth module for calling the google API and getting the score of the tweet. "The score of a Tweet's sentiment indicates the overall emotion of a Tweet" - Natural Language API Basics.
Fifth module is where the above mentioned modules are called to perform the analysis and the score is printed.
Output of the two programs are also mentioned in the text file along with the source code.

Github actions were added which involved adding a .yaml file, which checks out the pushed code, installs the software dependencies, and runs bats -v.

test_nlp2.py was created which contains the following units tests:

1.)Test to check whether get_sentiment_score() fn return a value between -1 and 1

2.)check the type of value returned by get_sentiment_score(tweet) fn

3.)checking whether clean_tweets(tweet) returns any tweets with hyperlinks in it

4.)if total_tweets varaiable is not of type int


import unittest
from nlp2 import *
class TestNLP(unittest.TestCase):
    def test_nlp(self):
        #test to check whether get_sentiment_score() fn return a value between -1 and 1
        self.assertLessEqual(get_sentiment_score(tweet),1)
        self.assertGreatEqual(get_sentiment_score(tweet),-1)
        #check the type of value returned by get_sentiment_score(tweet) fn
        self.assertRaises(TypeError,get_sentiment_score(tweet),True)
        #checking whether clean_tweets(tweet) returns any tweets with hyperlinks in it
        self.assertRegex("https://",clean_tweets(tweet))
        #if total_tweets varaiable is not of type int
        self.assertRaises(TypeError,search_tweets(keyword, total_tweets),True)

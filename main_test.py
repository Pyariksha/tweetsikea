import pytest
import tweepy
import main
from main import get_tweets_ikea, bq_load
from pandas.io import gbq
import pandas_gbq

class TestMain:
    def test_get_tweets(self):
        client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAADpAcAEAAAAAN9RKdHzdbTki26SRndWSkFNtZY8%3Ddllih5AeitkWwr9NitUkJRdyurMgDcBQeTZpawFOcaQ6EdK7z4')
        query = '#ikea -is:retweet lang:en'
        tweets_test = client.search_recent_tweets(query=query, tweet_fields=['created_at'], max_results=10)
        x = get_tweets_ikea(tweets_test)
        assert x.columns.to_list() == ['created_at', 'id', 'text']

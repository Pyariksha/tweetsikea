#import key modules
import tweepy
import pandas as pd
from pandas.io import gbq
import pandas_gbq

#load data into bigQuery table from df
def bq_load(key, value):
  """
  Function loads data into bq from pandas df.
  """
  project_name = 'sigma-scheduler-348710'#gcp project name
  dataset_name = 'ikea'
  table_name = key
  value.to_gbq(destination_table='{}.{}'.format(dataset_name, table_name), project_id=project_name, if_exists='append')#append tweets to table

#Bearer Token can be inserted from gcp functions environment variables for twitter api access
client = tweepy.Client(bearer_token='AAAAAAAAAAAAAAAAAAAAADpAcAEAAAAAN9RKdHzdbTki26SRndWSkFNtZY8%3Ddllih5AeitkWwr9NitUkJRdyurMgDcBQeTZpawFOcaQ6EdK7z4')

# Get tweets that contain the hashtag #ikea
# -is:retweet exclude retweets
# lang:en for the tweets in english
query = '#ikea -is:retweet lang:en'
#search tweets based on hashtag - 3 attributes selected (id, created_at, text)
tweets = client.search_recent_tweets(query=query, tweet_fields=['created_at'], max_results=100)

#define function to get tweets to be run in gcp cloud functions
def get_tweets_ikea(tweets):
    '''
    This function gets the tweets we want from '#ikea' and saves the 3 required attributes to a pandas dataframe.
    Input params: data and context - default for cloud functions triggered by gcs. param is request for http.
    '''
    try:
        list = []                       #initialize empty list
        for tweet in tweets.data:
            list.append(tweet)          #append each tweet to list
        df = pd.DataFrame(list)         #create dataframe from list
        df = df.drop_duplicates()       #drop duplicate tweets in dataframe -- good for batcch loads
        bq_load('ikea_table_data', df)  #write to bigquery table
        #no need for a return statement as the function output is a load run to BigQueary (runs the bq_load function)
        return df
    except:
        raise Exception('Error in function get_tweets_ikea.') #exception handling to seperate config/run failures from function code errors
        
get_tweets_ikea(tweets) #calls the function as every time gcp runs the function the bq table must update with appended tweets.
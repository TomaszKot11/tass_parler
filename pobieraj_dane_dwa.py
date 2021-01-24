import pandas as pd 
import numpy as np
import tweepy
import csv

consumer_key = 'qpO5XuPM1eZyOBDVcN9tWjNtc'
consumer_secret = 'mW0fSnkFq8F4fmLbtkSUyElu1DgViDXc1cuiNNO83dBIljiqQp'
access_token = '1340235807790149632-cB2YCYsMnkGTvChbJVL0yCLhxUiIXO'
access_token_secret = 'KuPWLZHLYNFZmuEziUsiG9mZNbof2ezigp4bSeBSvVyK2'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

df = pd.read_csv('./ua.csv', header=None)
ids_df = (df[df.columns[1]])

# delete the last element
ids_df.drop(ids_df.tail(1).index,inplace=True)
ids_df_split = np.split(ids_df, 40)
flipped_elements = np.flip(ids_df_split)
from_count = np.size(flipped_elements)

for count, split in enumerate(flipped_elements): 
  print("Step {}".format(count))
  csvFile = open("./following_pairs_{}_{}.csv".format(from_count-count, count), 'w+')
  csvWriter = csv.writer(csvFile)
  for id in split: 
    print("Id {} ".format(id))
    u = api.get_user(id)
    screen_name = u.screen_name
    print("Step: {}".format(count))
    for following in tweepy.Cursor(api.friends, screen_name).items(1000): 
      print("Step: {}".format(count))
      csvWriter.writerow([screen_name, following.screen_name])

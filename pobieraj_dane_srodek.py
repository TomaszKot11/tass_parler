import pandas as pd 
import numpy as np
import tweepy
import csv

consumer_key = '2QO7VoLUiSMDVwDApggTR7gUr'
consumer_secret = '8p7TbYH8wHNQwU077NEsfZ8hrObHX2FQk2DzH8JBVj8PHZFbCX'
access_token = '1340235807790149632-wi8pjWzkn8Y9snrIafvdkRtR4qnXOA'
access_token_secret = 'NbQMyWD9qWpK08udSuaiNLV4L4VTNIDVZDcpv3bqvyeCW'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

df = pd.read_csv('./ua.csv', header=None)
ids_df = (df[df.columns[1]])

# delete the last element
ids_df.drop(ids_df.tail(1).index,inplace=True)
ids_df_split = np.split(ids_df, 40)

for count, split in enumerate(ids_df_split): 
  print(count)
  if count >= 20 and count <= 29:
    print("Step {}".format(count))
    csvFile = open("./following_pairs_{}_middle.csv".format(count), 'w+')
    csvWriter = csv.writer(csvFile)
    for id in split: 
      print("Id {} ".format(id))
      u = api.get_user(id)
      screen_name = u.screen_name
      print("Step: {}".format(count))
      for following in tweepy.Cursor(api.friends, screen_name).items(1000): 
        print("Step: {}".format(count))
        csvWriter.writerow([screen_name, following.screen_name])

import pandas as pd 
import numpy as np
import tweepy
import csv

# consumer_key = '5bk4xeCa5n45zSMKcVKee6dRz'
# consumer_secret = 'zNpZnzPn7bvNBXJmLQw3UKnmqymTtVs3pcQ4zEvlHHUO1LSKOm'
# access_token = '1340235807790149632-odVF5edmxy3GtoI9t7Cqy3lnHQACZT'
# access_token_secret = 'oEUH8FbaznPM7ffUXlZ2fKx4bs36YhHtNLMaOdVqwK211'

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

# for count, split in enumerate(ids_df_split[11:]): 
#   try:
#     new_count = count + 11
#     print("Step {}".format(new_count))
#     csvFile = open("./following_pairs_{}.csv".format(new_count), 'w+')
#     csvWriter = csv.writer(csvFile)
#     for id in split: 
#       print("Id {} ".format(id))
#       u = api.get_user(id)
#       screen_name = u.screen_name
#       print("Step: {}".format(new_count))
#       for following in tweepy.Cursor(api.friends, screen_name).items(25): 
#         print("Step: {}".format(new_count))
#         csvWriter.writerow([screen_name, following.screen_name])
#   except tweepy.TweepError:
#     print('Failed to fetch the tweets for the user')

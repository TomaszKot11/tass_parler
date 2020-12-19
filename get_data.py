import cPickle
import os
import twitter  # https://github.com/ianozsvald/python-twitter

# Usage:
# $ # setup CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET
# as environment variables
# $ python get_data.py  # downloads friend and follower data to ./data

# Errors seen at runtime:
# raise URLError(err)
# urllib2.URLError: <urlopen error [Errno 104] Connection reset by peer>

DATA_DIR = "data"  # storage directory for friend/follower data

# list of screen names that we'll want to analyse
screen_names = ['ianozsvald', 'annotateio', 'morconsulting', 'fluffyemily',
                'jot', 'brouberol',
                'markpriestley', 'steeevem', 'lovedaybrooke',
                'jameshaycock', 'localben']

# api keys
# qpO5XuPM1eZyOBDVcN9tWjNtc
# api key secret
# mW0fSnkFq8F4fmLbtkSUyElu1DgViDXc1cuiNNO83dBIljiqQp

# Access token
# 1340235807790149632-cB2YCYsMnkGTvChbJVL0yCLhxUiIXO
# Access token secret
# KuPWLZHLYNFZmuEziUsiG9mZNbof2ezigp4bSeBSvVyK2
from dotenv import load_dotenv

load_dotenv()

def get_filenames(screen_name):
    """Build the friends and followers filenames"""
    return os.path.join(DATA_DIR, "%s.friends.pickle" % (screen_name)), os.path.join(DATA_DIR, "%s.followers.pickle" % (screen_name))

if __name__ == "__main__":
    print os.getenv('CONSUMER_KEY')
    t = twitter.Api(consumer_key=os.getenv('CONSUMER_KEY'),
                    consumer_secret=os.getenv('CONSUMER_SECRET'),
                    access_token_key=os.getenv('ACCESS_TOKEN_KEY'),
                    access_token_secret=os.getenv('ACCESS_TOKEN_SECRET'))
    print t.VerifyCredentials()

    print t.GetFollowers(screen_name='ianozsvald')
    # print "Downloading friends and followers for:", screen_names
    # for screen_name in screen_names:
    #     print screen_name
    #     fr_filename, fo_filename = get_filenames(screen_name)
    #     print "Checking for:", fr_filename, fo_filename
    #     if not os.path.exists(fr_filename):
    #         print "Getting friends for", screen_name
    #         fr = t.GetFriends(screen_name)
    #         cPickle.dump(fr, open(fr_filename, "w"), protocol=2)
    #     if not os.path.exists(fo_filename):
    #         print "Getting followers for", screen_name
    #         fo = t.GetFollowers(screen_name)
    #         cPickle.dump(fo, open(fo_filename, "w"), protocol=2)

#
# Mala uwaga: nie przesadzaj z requestami bo ci wywali limit ;)
#
# consumer
# CONSUMER_KEY=5bk4xeCa5n45zSMKcVKee6dRz
# CONSUMER_SECRET=zNpZnzPn7bvNBXJmLQw3UKnmqymTtVs3pcQ4zEvlHHUO1LSKOm
# ACCESS_TOKEN_KEY=1340235807790149632-odVF5edmxy3GtoI9t7Cqy3lnHQACZT
# ACCESS_TOKEN_SECRET=oEUH8FbaznPM7ffUXlZ2fKx4bs36YhHtNLMaOdVqwK211

# 2 aplikacja
#
# CONSUMER_KEY=qpO5XuPM1eZyOBDVcN9tWjNtc
# CONSUMER_SECRET=mW0fSnkFq8F4fmLbtkSUyElu1DgViDXc1cuiNNO83dBIljiqQp
# ACCESS_TOKEN_KEY=1340235807790149632-cB2YCYsMnkGTvChbJVL0yCLhxUiIXO
# ACCESS_TOKEN_SECRET=KuPWLZHLYNFZmuEziUsiG9mZNbof2ezigp4bSeBSvVyK2

#
# 3 apka
## customer
# 2QO7VoLUiSMDVwDApggTR7gUr
#8p7TbYH8wHNQwU077NEsfZ8hrObHX2FQk2DzH8JBVj8PHZFbCX
# tokens
#1340235807790149632-wi8pjWzkn8Y9snrIafvdkRtR4qnXOA
#NbQMyWD9qWpK08udSuaiNLV4L4VTNIDVZDcpv3bqvyeCW

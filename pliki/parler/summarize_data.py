import cPickle
import os
import simplejson as json

# output file once we've summarised the screen_names per users
ALL_NAMES = os.path.join(os.getcwd(), "data", "all_names.pickle")

print ALL_NAMES

def get_filenames(screen_name):
    """Build the friends and followers filenames"""
    return os.path.join(os.getcwd(), "data", "%s.friends.json" % (screen_name)), os.path.join(os.getcwd(), "data", "%s.followers.json" % (screen_name))

def get_names(sn):
    """Get a list of twitter followers"""
    fr_filename, fo_filename = get_filenames(screen_name)
    filename = fo_filename
    print 'Opening the JSON file named: ', filename
    with open(filename, 'r') as j:
     names = json.loads(j.read())
     return names
    return None


if __name__ == "__main__":
#     # summarise the screen_names from Twitter's JSON into a simple dictionary
    all_names = {}
    screen_names = ['Johnnyjoe1083', 'LHolden', 'BuddyDavis21', 'Compatriot']
    for screen_name in screen_names:
        all_names[screen_name] = set([sn['username'] for sn in get_names(screen_name)])

#     # we can get an overlapping set with something like this:
#     #set(all_names['annotateio']).intersection(set(all_names['ianozsvald']))

    cPickle.dump(all_names, open(ALL_NAMES, "w"), protocol=2)

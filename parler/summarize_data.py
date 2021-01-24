import cPickle
import os
import simplejson as json

ALL_NAMES = os.path.join(os.getcwd(), "data", "all_names.pickle")

def get_filenames(screen_name):
    return os.path.join(os.getcwd(), "data", "%s.friends.json" % (screen_name)), os.path.join(os.getcwd(), "data", "%s.followers.json" % (screen_name))

def get_names(sn):
    fr_filename, fo_filename = get_filenames(screen_name)
    filename = fo_filename
    with open(filename, 'r') as j:
     names = json.loads(j.read())
     return names
    return None


if __name__ == "__main__":
    all_names = {}
    screen_names = ['Johnnyjoe1083', 'LHolden', 'BuddyDavis21', 'Compatriot']
    for screen_name in screen_names:
        all_names[screen_name] = set([sn['username'] for sn in get_names(screen_name)])
    cPickle.dump(all_names, open(ALL_NAMES, "w"), protocol=2)

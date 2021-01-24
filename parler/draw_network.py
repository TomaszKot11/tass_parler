import pygraphviz
import networkx as nx
import cPickle
import pylab
import os

MAX_FOLLOWERS = 99900  # limit analysis to speed up our development iterations
MIN_EDGES_FOR_LABEL = 10

# load the follower networks
ALL_NAMES_SERIALIZED = os.path.join(os.getcwd(), "data", "all_names.pickle")
af = cPickle.load(open(ALL_NAMES_SERIALIZED))

################################
# Build a graph of all followers
################################
Gf = nx.Graph()

for screen_name, followers in af.items():
    some_followers = list(followers)[:MAX_FOLLOWERS]
    Gf.add_node(screen_name)
    Gf.add_nodes_from(some_followers)
    for follower in some_followers:
         Gf.add_edge(follower, screen_name)

print 1
posDefault = nx.nx_agraph.graphviz_layout(Gf, root=None, args="")
print 2
#posFrucht = nx.nx_agraph.graphviz_layout(Gf, prog='fdp', root=None, args="")


labels = {}
for node in Gf.nodes():
  labels[node] = ""
  if len(Gf.edges(node)) > MIN_EDGES_FOR_LABEL:
    labels[node] = node

print 'Before drawing'

# default one
nx.draw_networkx(Gf, posDefault, with_labels=True, alpha=0.2, labels=labels, font_size=20, font_family='sans-serif')
pylab.axis("off")
pylab.title("Parler - Kamady Kawai")

pylab.show()

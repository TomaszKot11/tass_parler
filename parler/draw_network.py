# -*- coding: utf-8 -*-
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

# # shave off followers who are follow nobody in our inner network, so NetworkX
# # can plot a sane number of people at the edge of the graph
# MAX_WITH_0_FOLLOWERS = 40
# for screen_name, followers in af.items():
#     nbr_with_no_followers = 0
#     for follower in followers:
#         edges_of_connected_node = Gf.edges(follower)
#         if len(edges_of_connected_node) == 1:
#             if nbr_with_no_followers == MAX_WITH_0_FOLLOWERS:
#                 Gf.remove_node(follower)
#             else:
#                 nbr_with_no_followers += 1
#     print "Capping:", screen_name, nbr_with_no_followers



pos = nx.nx_agraph.graphviz_layout(Gf, root=None, args="")

labels = {}
for node in Gf.nodes():
  labels[node] = ""
  if len(Gf.edges(node)) > MIN_EDGES_FOR_LABEL:
    labels[node] = node

nx.drawing.nx_pylab.draw_kamada_kawai(Gf, with_labels=True, alpha=0.2, labels=labels, font_size=20, font_family='sans-serif')

pylab.axis("off")
pylab.title("Parler")
pylab.show()

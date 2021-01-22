# -*- coding: utf-8 -*-
import pygraphviz
import networkx as nx
import cPickle
import pylab
import summarise_data

MAX_FOLLOWERS = 99900  # limit analysis to speed up our development iterations

# load the follower networks
af = cPickle.load(open(summarise_data.ALL_NAMES))

print af

# build a graph of all followers
Gf = nx.Graph()
for screen_name, followers in af.items():
    some_followers = list(followers)[:MAX_FOLLOWERS]
    Gf.add_node(screen_name)
    Gf.add_nodes_from(some_followers)
    for follower in some_followers:
        print 'Adding the edge'
        Gf.add_edge(follower, screen_name)

# shave off followers who are follow nobody in our inner network, so NetworkX
# can plot a sane number of people at the edge of the graph
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


print 'Positions'

print '1'
posDefault = nx.nx_agraph.graphviz_layout(Gf, prog='neato', root=None, args="")
print '2'
posFrucht = nx.nx_agraph.graphviz_layout(Gf, prog='fdp', root=None, args="")
print '3'
posSpectacular = nx.spectral_layout(Gf) # wartosci wlasne


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

# wartosci wlasne macierzy
nx.draw_networkx(Gf, posSpectacular, with_labels=True, alpha=0.2, labels=labels, font_size=20, font_family='sans-serif')
pylab.axis("off")
pylab.title("Parler - wartosci wlasne ")

pylab.show()


nx.draw_networkx(Gf, posFrucht, with_labels=True, alpha=0.2, labels=labels, font_size=20, font_family='sans-serif')
pylab.axis("off")
pylab.title("Parler - Fruchterman")

pylab.show()


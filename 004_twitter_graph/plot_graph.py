"""plot social graph

use options

    -h - for help
    -l - to plot labels
"""

import networkx as nx
import matplotlib.pyplot as plt
import simplejson as json
from pylab import array
from write_edgelist_numbers import write_edgelist_numbers

import os
import sys
import getopt

argv = sys.argv
try:
    # options that require arguments are followed by :
    opts, args = getopt.getopt(argv[1:], "l",['--help'])
except getopt.error, msg:
     raise Usage(msg)

is_plotting_labels = False

# process options
for o, a in opts:
    if o in ("-h", "--help"):
        print __doc__
        sys.exit(0)
    if o == '-l':
        is_plotting_labels = True

if os.path.exists('data/level.txt'):
    from print_communities import label2cluster


G=nx.DiGraph()

file = open('data/members.txt','r')
members = {}
for user in file:
    user_name = user.strip().lower()
    members[user_name] = []
    
for p in members:
    G.add_node(p)

f = open('data/friends_graph.txt')
members = json.load(f)
f.close()

for m in members:
    for f in members[m]:
        if not m == f:
            if f in members:
                # G.add_edge(m,f,weight=members[m][f])
                G.add_edge(m,f)

for m in members:
    if max(G.in_degree(m),G.out_degree(m)) < 1:
        G.remove_node(m)

#pos=nx.graphviz_layout(G)
#import random
#for m in G:
#    pos[m] = (random.uniform(-1,1),random.uniform(-1,1))
# for p in pos:
#     pos[p] = array(pos[p])
# print pos
# pos=nx.spring_layout(G,dim=2,weighted=True,pos=pos)

#edgewidth=[0 for v in G]
#nx.draw(G,pos,linewidths=0,width=edgewidth,node_size=1,font_size=16,node_color='r',with_labels=False)
#nx.draw_networkx_edges(G,pos,alpha=0.1,node_size=0,width=1,edge_color='m')

# nx.draw(G,pos=nx.spectral_layout(G), nodecolor='r',edge_color='b')
pos=nx.graphviz_layout(G)
# pos=nx.graphviz_layout(G,prog="twopi",root='garaiko')
pos=nx.spring_layout(G,iterations=100,pos=pos)

if os.path.exists('data/level.txt'):
    node_color = [label2cluster[n] for n in G]
else:
    node_color = [(1,0,0) for n in G]

if is_plotting_labels:
    fig = plt.figure(figsize=(22,22))
    nodesize=100
    nx.draw_networkx_nodes(G,pos,node_size=nodesize,node_color=node_color,alpha=0.4,linewidths=0)
    nx.draw_networkx_edges(G,pos,alpha=0.1,node_size=0,width=1,edge_color='k')
    nx.draw_networkx_labels(G,pos,fontsize=10)
else:
    fig = plt.figure(figsize=(8,8))
    nx.draw_networkx_nodes(G,pos,node_color=node_color,alpha=0.3)
    nx.draw_networkx_edges(G,pos,alpha=0.3,node_size=0,width=1,edge_color='k')

#for p in pos: # raise text positions
#    pos[p][1]+=0.07
# g = nx.draw_networkx_labels(G,pos)

pr = nx.pagerank(G,alpha=0.85,max_iter=200)

pr_pair = zip(pr.values(),pr.keys())
pr_pair.sort(reverse=True)

i = 0
sum = 0
n_top = 20
for pr in pr_pair:
    i+=1
    print i,pr[1],pr[0]
    sum += pr[0]
    if i >= n_top:
        print sum
        break

print nx.number_strongly_connected_components(G)
#print nx.center(sc)
#print nx.diameter(sc)

# identify largest connected component
Gcc=nx.strongly_connected_component_subgraphs(G)
G0=Gcc[0]
print dir(G0)
print G0.nodes()
print 'len G0',len(G0)
nx.draw_networkx_edges(G0,pos,
                       with_labels=False,
                       edge_color='r',
                       alpha = 0.1
                    )
# show other connected components
for Gi in Gcc[1:]:
   if len(Gi)>1:
      nx.draw_networkx_edges(Gi,pos,
                             with_labels=False,
                             edge_color='b',
                             alpha = 0.1
                             )


nx.write_pajek(G,"data/twitter.net")

write_edgelist_numbers(G,"data/twitter.edgelist","data/edgelist_conversion.txt")

plt.axis('off')
plt.savefig('graph.png',dpi=72)
plt.show()

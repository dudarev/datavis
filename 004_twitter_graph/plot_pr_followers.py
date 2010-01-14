"""plot pagerank vs. number of members mentioning that member"""

title = "Donetsk"
figure_file_name = "pr_vs_followers_donetsk.png"
# what points to label
followers_min = 9
pr_min = 0.02
# figure parameters
x_max = 25 
y_max = 0.07
shift_more = ('gasique','lapidarius')

import networkx as nx
import matplotlib.pyplot as plt
import simplejson as json
from pylab import array

# fill the graph
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
                print members[m][f]

# remove nodes that are not connected
for m in members:
    if max(G.in_degree(m),G.out_degree(m)) < 1:
        G.remove_node(m)

#data for plotting
pr = nx.pagerank(G,alpha=0.85,max_iter=200)
n_followers = dict([(m,G.in_degree(m)) for m in G])

pr_ar = [pr[m] for m in G]
n_followers_ar = [n_followers[m] for m in G]
m_ar = [m for m in G]

# plotting
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.transforms import offset_copy

fig = plt.figure()
ax = plt.axes([0.15, 0.15, 0.75, 0.75])

transOffset = offset_copy(ax.transData, fig=fig, x = 0.05, y=0.10, units='inches')
transOffset_more = offset_copy(ax.transData, fig=fig, x = 0.05, y=0.25, units='inches')

for x, y, t in zip(n_followers_ar,pr_ar,m_ar):
    plt.plot((x,),(y,), 'ro')
    if y > pr_min and x > followers_min:
        if t in shift_more:
            plt.text(x, y, t, transform=transOffset_more,horizontalalignment="right",fontsize=16)
        else:
            plt.text(x, y, t, transform=transOffset,horizontalalignment="right",fontsize=16)

plt.ylim(0,y_max)
plt.xlim(0,x_max)

labels = ax.get_xticklabels()
plt.setp(labels, fontsize=18)
labels = ax.get_yticklabels()
plt.setp(labels, fontsize=18)
plt.xlabel('# of followers',fontsize=20);
plt.ylabel('PageRank',fontsize=20);
plt.title(title,fontsize=22);

plt.savefig(figure_file_name,dpi=54)
plt.show()

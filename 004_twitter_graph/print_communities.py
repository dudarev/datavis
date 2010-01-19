import simplejson as json
import networkx as nx

# load label to number conversion

label2number = json.loads(open('data/edgelist_conversion.txt').read())
number2label = {}
for l,n in label2number.items():
    number2label[n] = l

# load cluster correspondence

number2cluster = {}

file = open('data/level.txt')
for line in file:
    n,c = map(int,line.strip().split(' '))
    number2cluster[n] = c

# get lable to cluster correspondence

label2cluster = {}

for l,n in label2number.items():
    label2cluster[l] = number2cluster[n]

print label2cluster

# get cluster members

cluster2labels = {}
for n,c in number2cluster.items():
    if c in cluster2labels:
        cluster2labels[c].append(number2label[n])
    else:
        cluster2labels[c] = [number2label[n]]

print cluster2labels

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

pr = nx.pagerank(G)

cluster2pagerank = {}

for c,labels in cluster2labels.items():
    cluster2pagerank[c] = 0
    for l in labels:
        cluster2pagerank[c] += pr[l]

print cluster2pagerank

cluster_pr_pairs = zip(cluster2pagerank.values(),cluster2pagerank.keys())
cluster_pr_pairs.sort(reverse=True)

def print_two_members(members_list,pr):
    pr_list = [pr[m] for m in members_list]
    member_pr_pairs = zip(pr_list,members_list)
    member_pr_pairs.sort(reverse=True)
    first_two = [m for pr,m in member_pr_pairs][0:2]
    print ' ', first_two[0], '  ', first_two[1], ' ...'

print 40*'-'
from classify_cluster import classify_cluster

for cp in cluster_pr_pairs:
    print cp, len(cluster2labels[cp[1]])
    print_two_members(cluster2labels[cp[1]],pr)
    classify_cluster(cluster2labels[cp[1]])
    print '\n\n'


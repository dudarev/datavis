import networkx as nx
import simplejson as json

def write_edgelist_numbers(G,file_edgelist,file_conversion):

    fe = open(file_edgelist,'w') 
    fc = open(file_conversion,'w')

    G = nx.convert_node_labels_to_integers(G,discard_old_labels=False)
    for m in G:
        for n in G[m]:
            fe.write('%d %d\n' % (m,n))

    fc.write(json.dumps(G.node_labels))

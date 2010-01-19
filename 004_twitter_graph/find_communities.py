import os

print 40*'-'
print 'preparing data'
os.system('./convert -i data/twitter.edgelist -o data/graph.bin')
print 40*'-'
print 'finding communities'
os.system('./community data/graph.bin -l -1 > data/graph.tree')
print 40*'-'
print 'information about communities'
os.system('./hierarchy data/graph.tree')
print 40*'-'
print 'save node to community correspondence'
os.system('./hierarchy data/graph.tree -l 2 > data/level.txt')

print 'ok'

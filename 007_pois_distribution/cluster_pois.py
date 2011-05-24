import simplejson as json

f = open('pois_xy.json','r') 
data = f.read() 
pois = json.loads(data)

x = []
y = []
xy = []

for p in pois:
    x.append(p['x'])
    y.append(p['y'])
    xy.append([p['x'], p['y']])

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import mlpy

xy = np.array(xy)
hc = mlpy.HCluster(link="single")
hc.compute(xy)
print hc.heights
jump_length = 1 
cut = hc.cut(jump_length)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x, y, c=cut, cmap='jet', alpha=0.5)
# http://stackoverflow.com/questions/250357/smart-truncate-in-python
def smart_truncate(content, length=100, suffix='...'):
    if len(content) <= length:
        return content
    else:
        return ' '.join(content[:length+1].split(' ')[0:-1]) + suffix
for p in pois:
    if p['y'] > 14:
        t = ax.text(p['x'], p['y'], p['name'])
    if p['y'] < 1:
        t = ax.text(p['x'], p['y'], p['name'])
    if p['x'] < 0.1:
        t = ax.text(p['x'], p['y'], p['name'])
    if p['x'] > 32:
        t = ax.text(p['x'], p['y'], smart_truncate(p['name'], length=10))
    if p['x'] < 11 and p['y'] > 7 and p['x'] > 6:
        t = ax.text(p['x'], p['y'], p['name'])
    if p['x'] > 28 and p['y'] > 10:
        t = ax.text(p['x'], p['y'], smart_truncate(p['name'], length=20))

plt.ylim([-1,17])
plt.xlim([-2,42])

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.savefig('007_pois_cluster.png', dpi=72)

print cut

cut_count = {}
for c in cut:
    cut_count[c] = cut_count.get(c,0) + 1
print cut_count

from matplotlib import cm

fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111)
x = [x for x in cut_count]
max_c = max(x)
color = [cm.jet(cm.jet.N*c/max_c) for c in cut_count]

decorated_lists = [ [cut_count[x], x, color[x]] for x in cut_count]
decorated_lists.sort(reverse=True)
decorated_lists=decorated_lists[:5]

cut_count = [i[0] for i in decorated_lists]
x = [i[1] for i in decorated_lists]
color = [i[2] for i in decorated_lists]

ax2.bar([i for i in range(len(cut_count))], cut_count, color=color)

ax2.get_xaxis().set_visible(False)
labels = ax2.get_yticklabels()
plt.setp(labels, fontsize=18)
plt.xlim([-0.25,5.05])

plt.savefig('007_clusters_numbers.png', dpi=54)

plt.show()

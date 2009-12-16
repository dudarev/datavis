import os
from numpy import *
from pylab import *

file = open('data/followers.txt','r')

first = True

for user in file:

    user_name = user.strip()
    print user_name
    if not os.path.exists('data/%s.txt' % user_name):
        continue
    file_counts = open('data/%s.txt' % user_name,'r')
    line = file_counts.read().strip()
    if not line:
        file_counts.close()
        continue
    data = line.split(',')
    counts_hours = array(map(int,data[1:]))
    if first:
        counts_total = counts_hours
        first = False
    else:
        counts_total = counts_total + counts_hours
    print counts_hours

ax = axes([0.15, 0.15, 0.75, 0.75])

hours = arange(24)
fraction = counts_total * 100. / sum(counts_total)
bar(hours, fraction,width=1,edgecolor='blue')

xlim(0,24)
xticks(range(0, 24, 2))

labels = ax.get_xticklabels()
setp(labels, fontsize=20)
labels = ax.get_yticklabels()
setp(labels, fontsize=20)
 
xlabel('hours GMT',fontsize=24);
ylabel('fraction, %',fontsize=24);

# plot average
fraction_uniform = 100./24.
p2 = plot([0,24],[fraction_uniform,fraction_uniform],'r--')

savefig('003_tweetingplaces.png',dpi=36)

show()

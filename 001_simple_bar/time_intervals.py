# plots simple bar plot

from pylab import *

intervals = [10, 20, 2, 10, 10, 19, 10, 9, 10, 21, 16, 13]
x = arange(len(intervals)) + 1

# print simple statistics
print average(intervals)
print median(intervals)

ax = axes([0.15, 0.15, 0.75, 0.75])

bar(x, intervals)

# plot average
p2 = plot([min(x),max(x)+1],[average(intervals),average(intervals)],'r--')

xlim(min(x),max(x))

labels = ax.get_xticklabels()
setp(labels, fontsize=20)
labels = ax.get_yticklabels()
setp(labels, fontsize=20)

xlabel('step number',fontsize=24);
ylabel('time spent on each step, min',fontsize=24);

savefig('001_simple_bar.png')
show()

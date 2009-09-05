# plots simple bar plot

from pylab import *

intervals = [10, 20, 2, 10, 10, 19, 10, 9, 10, 21, 16, 13]
x = arange(len(intervals))

# print simple statistics
print average(intervals)
print median(intervals)

bar(x, intervals)
savefig('001_simple_bar.png')
show()

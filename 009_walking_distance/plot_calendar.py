import csv
import re


date_re = re.compile('\d+_\d+_\d+')

csv_reader = csv.reader(open('trips.csv', 'r'))

# skip the first line
csv_reader.next()

day_distance = {}

for row in csv_reader:
    # parse date
    date_str = row[0]
    y,m,day = date_re.match(date_str).group().split('_')
    day = int(day)
    day_distance[day] = day_distance.get(day,0) + float(row[1])

print len([i for i in day_distance if day_distance[i]>5000])
print len([i for i in day_distance if day_distance[i]>4000])
print len([i for i in day_distance if day_distance[i]>3000])

import calendar

m = calendar.month(2012,6)
print m

lines = m.split('\n')
print lines

from matplotlib.font_manager import FontProperties
from pylab import *

alignment = {'horizontalalignment':'center', 'verticalalignment':'baseline'}

figure(figsize=(8,8))
axes([0, 0, 1, 1])

font0 = FontProperties(size=18)

font = font0.copy()

y = 0.9
dy = 0.15

x0 = 0.2
dx = 0.1

font.set_size(24)
t = text(0.5, y, lines[0].strip(), fontproperties=font, **alignment)
font.set_size(22)

for l in lines[2:]:
    y = y - dy
    for i in range(7):
        day = l[i*3:i*3+2].strip()
        color = 'k'
        print 'day:', day
        if day and day_distance.get(int(day),0) > 4000:
            color = 'r'
            font.set_weight('bold')
        t = text(x0 + i*dx, y, l[i*3:i*3+2].strip(), fontproperties=font, 
                color=color, **alignment)
        font.set_weight('normal')

savefig('walking_calendar.png',dpi=72)
axis('off')

show()

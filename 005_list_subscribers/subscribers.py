# read csv file with joining dates
# count number of new subscribers in each month
# plot

import csv
from datetime import date,timedelta

reader = csv.reader(open("cnc-donetsk.csv"))

# skip first two lines
title = reader.next()
description = reader.next()

# get indexes of year, month and day
year_index = description.index('join year')
month_index = description.index('join month')
day_index = description.index('join day')

date_min = None
date_max = None

n_per_month = {}

for row in reader:
    year = int(row[year_index])
    month = int(row[month_index])
    day = int(row[day_index])

    time_tuple = (year, month, day)
    d = date(*time_tuple[0:3])
    if not date_min or date_min > d:
        date_min = d
    if not date_max or date_max < d:
        date_max = d

    first_day = d.replace(day=1) 
    n_per_month[first_day] = n_per_month.get(first_day,0) + 1

print repr(date_min)
print repr(date_max)
print date_max - date_min

# based on http://www.ianlewis.org/en/python-date-range-iterator
def date_month_iterator(from_date=None, to_date=None):
    """iterator that return the first day of month for months between from_data and to_date from_date month including"""
    from_date = from_date or datetime.now()
    from_date = from_date.replace(day=1)
    while to_date is None or from_date <= to_date:
        yield from_date
        if from_date.month == 12:
            from_date = date(from_date.year+1,1,1)
        else:
            from_date = date(from_date.year,from_date.month+1,1)
    return

n_per_month_list = []
dates_list = []

for d in date_month_iterator(date_min, date_max):
    n_per_month_list.append( n_per_month.get(d,0) )
    dates_list.append(d)

print n_per_month_list

# based on http://stackoverflow.com/questions/2216273/irregular-matplotlib-date-x-axis-labels

import matplotlib.ticker as ticker
from pylab import *

ax = axes([0.15, 0.22, 0.75, 0.75])

plot(n_per_month_list)

def format_date(x, pos=None):
    date = dates_list[int(x)]
    if date.month % 2 == 0:
        return ''
    if date.month == 1: 
        return date.strftime('%b %Y')
    else: return date.strftime('%b')

xAxis = ax.xaxis
xAxis.set_major_locator(ticker.FixedLocator([i for i in range(0,len(n_per_month_list))]))
xAxis.set_major_formatter(ticker.FuncFormatter(format_date))
for tl in xAxis.get_ticklabels():
      tl.set_rotation(70)

yAxis = ax.yaxis
yAxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: str(x) if x%2 == 0 else ''))

xlim(0,len(n_per_month_list)-1)
xticks(range(1, len(n_per_month_list)))
yticks(range(0, 18))

labels = ax.get_xticklabels()
setp(labels, fontsize=14)
labels = ax.get_yticklabels()
setp(labels, fontsize=14)
 
xlabel('Month',fontsize=20);
ylabel('New subscribers',fontsize=20);

grid()

savefig('005_subscribers.png',dpi=54)

show()

"""parses gowalla checkins and saves only different places to
stamps.json"""

import os
import simplejson as json

from BeautifulSoup import BeautifulSoup as bs

data = []
data_dict = {}

file_name = "checkins.html"

soup = bs(open(file_name).read())

checkins = soup.findAll("div", {"class": "check-in"})
for c in checkins:
    links = c.findAll("a")
    for l in links:
        if 'spots' in l['href']:
            if not l['href'] in data_dict:
                print l['title']
                data_dict[l['href']] = l['title']

for k in data_dict:
    data.append({
        "name": data_dict[k],
        "link": k,
        })

f = open("stamps.json",'w')
f.write(json.dumps(data))
f.close()

print "Total number of stamps: %d" % len(data)

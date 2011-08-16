import os
import simplejson as json

from BeautifulSoup import BeautifulSoup as bs

data = []

file_name = "stamps.html"

soup = bs(open(file_name).read())
results = soup.find("div", {"id": "content"})
if results:
    names = results.findAll("a", {"class": "name"})
    for n in names:
        data.append({
            "name": n.contents[0].strip(),
            "link": n['href'],
            })
        print n.contents[0].strip()

f = open("stamps.json",'w')
f.write(json.dumps(data))
f.close()

print "Total number of stamps: %d" % len(data)

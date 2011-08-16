"""parses HTML files of points and creates KML
See options below. Some variations:

KML file without images (just pins):
    python create_kml.py -n -o stamps_no_image.kml

Debug mode (only 10 points):
    python create_kml.py -d
"""

import re
import os, sys
import simplejson as json

from BeautifulSoup import BeautifulSoup as bs

import simplekml
kml = simplekml.Kml()

from optparse import OptionParser

parser = OptionParser()
parser.add_option("-n", "--noimage", dest="image", default=True, action='store_false')
parser.add_option('-o', dest='file_name', default="stamps.kml")
parser.add_option('-d', "--debug", dest='debug', default=False, action='store_true')
(opts, args) = parser.parse_args(sys.argv)


data_dir = "data/spots"
file_name_points = "stamps.json"

data = json.loads(open(file_name_points, 'r').read())
files_downloaded = os.listdir(data_dir)

import html5lib
from html5lib import treebuilders

count = 1
for d in data:
    spot_id = re.search("/([^/]*$)", d['link']).group(1)
    print spot_id, d['name']
    file_name = "%s.html" % spot_id
    file_name = os.path.join(os.getcwd(), data_dir)
    file_name = os.path.join(file_name, "%s.html" % spot_id)

    f = open(file_name, "rb")
    parser = html5lib.HTMLParser(tree=treebuilders.getTreeBuilder("beautifulsoup"))
    soup = parser.parse(f, encoding="utf-8")

    name = soup.find("meta", {"property": "og:title"})['content'].encode('utf-8')
    print name
    lat = soup.find("meta", {"property": "og:latitude"})['content']
    lon = soup.find("meta", {"property": "og:longitude"})['content']
    image_url = soup.find("meta", {"property": "og:image"})['content']

    pnt = kml.newpoint(name=name,
                       description="<a href='%s'>Gowalla page</a>" % d['link'],
                       coords=[(lon, lat)])

    if opts.image:
        # pnt.iconstyle.scale = 2  # Icon twice as big
        pnt.iconstyle.icon.href = image_url
    
    print lat, lon

    count += 1

    if opts.debug:
        if count > 10:
            break

    print '-------'

kml.save(opts.file_name)

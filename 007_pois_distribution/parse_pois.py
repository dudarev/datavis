"""
parse osm file and save array of POIs in the format:
    [{"name": "name","x": x,"y": y],...]
where x,y are in kilometers counted from minimum latitude and longitude for all POIs
"""

from xml.etree  import cElementTree as etree
import simplejson as json

file_name = "donetsk.osm"

data = open(file_name,'r')

pois = []
lat_average = 0

time_format = "%Y-%m-%dT%H:%M:%SZ"

nodes_dict = {}

lat_min = 90
lon_min = 180

def update_min(lat, lon, lat_min, lon_min):
    if lat_min > lat:
        lat_min = lat
    if lon_min > lon:
        lon_min = lon
    return lat_min, lon_min

users_dict = {}

for event, elem in etree.iterparse(data):
    
    if elem.tag == 'node':
        tags = elem.findall('tag')
        id = elem.attrib['id']
        user = elem.attrib['user']
        users_dict[user] = users_dict.get(user, 0) + 1
        # all nodes are in dict because they are referenced in ways later
        nodes_dict[id] = elem
        if tags:
            if len(tags)==1 and tags[0].attrib['k']=='created_by':
                continue
            tags_dict = {}
            for t in tags:
                tags_dict[t.attrib['k']] = t.attrib['v']
            # ignore if the node is not named
            name = tags_dict.get('name', None)
            if not name:
                continue
            if 'highway' in tags_dict:
                print 'HIGHWAY'
                print name
            print [t for t in tags_dict]
            lat = float(elem.attrib['lat'])
            lon = float(elem.attrib['lon'])
            lat_min, lon_min = update_min(lat, lon, lat_min, lon_min)
            pois.append({'name': name, 'lat': lat, 'lon': lon})
            lat_average += lat

    if elem.tag == 'way':
        nds = elem.findall('nd')
        # if closed way
        if nds[0].attrib['ref'] == nds[-1].attrib['ref']:
            tags = elem.findall('tag')
            if tags:
                if len(tags)==1 and tags[0].attrib['k']=='created_by':
                    continue
                tags_dict = {}
                for t in tags:
                    tags_dict[t.attrib['k']] = t.attrib['v']
                # ignore if the way is not named
                name = tags_dict.get('name', None)
                if not name:
                    continue
                print [t for t in tags_dict]
                # find coordinates
                lat = 0.
                lon = 0.
                # do not count last node because it repeats the first
                for n in nds[:-1]:
                    node_id = n.attrib['ref']
                    node = nodes_dict[node_id]
                    lat += float(node.attrib['lat'])
                    lon += float(node.attrib['lon'])
                l = len(nds) - 1.
                if l > 0:
                    lat = lat/l
                    lon = lon/l
                lat_min, lon_min = update_min(lat, lon, lat_min, lon_min)
                pois.append({'name': name, 'lat': lat, 'lon': lon})
                lat_average += lat

print ''
print lat_min, lon_min

from math import cos, pi

# http://en.wikipedia.org/wiki/Latitude
# http://en.wikipedia.org/wiki/Longitude
# http://en.wikipedia.org/wiki/Longitude#Degree_length
delta_degree = 111 # km
delta_lat = delta_degree
lat_average = lat_average/len(pois)
delta_lon = delta_degree * cos( lat_average * pi/180 )
print delta_lat, delta_lon

for p in pois:
    x = (p['lon'] - lon_min) * delta_lon
    y = (p['lat'] - lat_min) * delta_lon
    print p['name'], x, y
    p['x'] = x
    p['y'] = y

f = open("pois_xy.json", 'w')
f.write(json.dumps(pois))
f.close()

users_list = [[users_dict[user],user] for user in users_dict]
users_list.sort(reverse=True)

user_url = "http://www.openstreetmap.org/user/"

for u in users_list:
    print u[0], "%s%s" % (user_url, u[1])

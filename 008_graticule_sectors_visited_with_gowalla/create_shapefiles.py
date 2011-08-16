from BeautifulSoup import BeautifulSoup as bs
from find_sector import find_polygon, find_sector
import shapefile

file_name = "stamps.kml"

print "reading stamps.kml"
soup = bs(open(file_name).read())

placemarks = soup.findAll("placemark")

sectors = set()

w = shapefile.Writer()
w = shapefile.Writer(shapefile.POLYGON)
w.field('NAME','C','40')

for p in placemarks:
    coord = p.find("point").find("coordinates")
    lon, lat, h = coord.contents[0].split(',')
    sector = find_sector(float(lon), float(lat))
    if not sector in sectors:
        sectors.add(sector)
        poly = find_polygon(float(lon), float(lat))
        w.poly(parts=[
            poly
            ])
        w.record(str(sector))

w.save('polygon')

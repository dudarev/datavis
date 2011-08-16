import csv
import shapefile

reader = csv.reader(open("cities15000.txt"), delimiter='\t')
writer = csv.writer(open("cities_over_1M.txt", 'w'), delimiter='\t')

# index of population and country in the file
population_index = 14
country_index = 8
lat_index = 4
lon_index = 5
name_index = 2

w = shapefile.Writer()
w = shapefile.Writer(shapefile.POINT)
w.field('NAME','C','40')

for row in reader:
    print row[population_index]
    if int(row[population_index]) > 1e6:
        lat = float(row[lat_index])
        lon = float(row[lon_index])
        w.point(lon, lat)
        w.record(row[name_index])

w.save('cities')

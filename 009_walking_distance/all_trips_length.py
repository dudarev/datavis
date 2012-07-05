import os
import csv
from datetime import timedelta

from pygpx import GPX

def trip_length_and_duration(file_name):
    duration = timedelta(seconds=0)
    open(file_name, 'r')
    gpx = GPX(open(file_name))
    distance = gpx.distance()
    duration = gpx.duration()
    return distance, duration.seconds

csv_file = open('trips.csv', 'w')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(('file name', 'length [m]', 'duration [sec]'))

for root, dirs, files in os.walk('data/'):
    for f in files:
        if f.endswith('.gpx'):
            l, d = trip_length_and_duration(os.path.join('data/',f))
            print f, l, d
            csv_writer.writerow((f, l, d))

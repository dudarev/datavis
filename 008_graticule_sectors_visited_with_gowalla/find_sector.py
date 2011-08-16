# -*- coding: utf8 -*-

"""Find sector for coordinates

sector is a tuple (x,y) of lower right corner of the 1 degree graticule
convention here: coordinates are in x,y order (lon,lat)
in function variables and elsewhere
"""

from math import floor

def find_sector(lon, lat):
    return (int(floor(lon)), int(floor(lat)))

def find_polygon(lon, lat):
    x, y = find_sector(lon, lat)
    return [[x, y], [x, y+1], [x+1, y+1], [x+1, y], [x, y]]

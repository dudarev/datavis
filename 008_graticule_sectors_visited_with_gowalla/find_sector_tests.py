# -*- coding: utf8 -*-

"""Find sector for coordinates
"""

import unittest
from find_sector import find_sector, find_polygon


class FindSectorsTests(unittest.TestCase):

    def test_simple(self):
        """testing that lon=37.4 lat=48.1 correspond to sector (37,48)
        """
        lon = 37.4
        lat = 48.1 
        self.assertEqual(find_sector(lon, lat), (37, 48))

    def test_negative(self):
        lon = -12.234
        lat = -0.1
        self.assertEqual(find_sector(lon, lat), (-13, -1))

    def test_integer(self):
        lon = -12
        lat = -0
        self.assertEqual(find_sector(lon, lat), (-12, 0))


class FindPolygonsTests(unittest.TestCase):

    def simple_test(self):
        lon = 37.4
        lat = 48.1 
        correct_polygon = [[37, 48], [37, 49], [38, 49], [38, 48], [37, 48]]
        self.assertEqual(find_polygon(lon, lat), correct_polygon)


if __name__ == '__main__':
    unittest.main()

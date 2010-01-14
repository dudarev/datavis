# -*- coding: utf8 -*-
"""on a page url_page
finds all links that contain twitter.com/member and 
saves members lists to data/members.txt"""

import urllib2
from BeautifulSoup import BeautifulSoup

url_page = 'http://ukrtweet.com.ua/?page_id=10'
file_members = 'data/members.txt'

usock = urllib2.urlopen(url_page)
html = usock.read()
usock.close()

count = 0

soup = BeautifulSoup(html)
links = soup.findAll('a')
f = open(file_members,'w')

for l in links:
    href = l['href']
    if 'twitter.com' in href:
        pos = href.rfind('/')+1
        f.write(href[pos:]+'\n')
        count += 1

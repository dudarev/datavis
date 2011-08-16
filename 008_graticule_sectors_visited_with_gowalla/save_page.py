import urllib2

def save_page(url, filename):
    usock = urllib2.urlopen(url)
    data = usock.read()
    usock.close()
    fp = open(filename, 'w')
    fp.write(data)
    fp.close()

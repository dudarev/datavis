import re
import os
from time import sleep
import simplejson as json

from save_page import save_page

data_dir = "data/spots"

data = json.loads(open('stamps.json', 'r').read())
files_downloaded = os.listdir(data_dir)

count = 1
for d in data:
    spot_id = re.search("/([^/]*$)", d['link']).group(1)
    print count
    print spot_id
    file_name = "%s.html" % spot_id
    if file_name in files_downloaded:
        print "Already exists"
    else:
        file_name = os.path.join(os.getcwd(), data_dir)
        file_name = os.path.join(file_name, "%s.html" % spot_id)
        save_page(d['link'], file_name)
        sleep(2)
    count += 1

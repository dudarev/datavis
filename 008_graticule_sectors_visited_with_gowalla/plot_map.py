from matplotlib.mlab import prctile_rank
from mpl_toolkits.basemap import Basemap, shiftgrid
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from matplotlib.patches import Polygon

# create new figure
fig=plt.figure(figsize=(8,6))

# setup lambert azimuthal equal area basemap.
# lat_ts is latitude of true scale.
# lon_0,lat_0 is central point.
m = Basemap(width=4500000,height=3000000,
            resolution='i',projection='laea',\
            lat_ts=48,lat_0=48,lon_0=20.)

# transform to nx x ny regularly spaced native projection grid
nx = int((m.xmax-m.xmin)/20000.)+1; ny = int((m.ymax-m.ymin)/20000.)+1
# get current axis instance.
ax = plt.gca()
pos = ax.get_position()
l, b, w, h = pos.bounds
plt.axes(ax)  # make the original axes current again
m.drawcountries()

def lat2str(step=5):
    def lat2str_aux(deg):
        if deg % step == 0:
            dir = 'N'
            if deg < 0:
                dir = 'S'
            return (u"%d\N{DEGREE SIGN} %s") % (np.abs(deg), dir)
        return ''
    return lat2str_aux

def lon2str(step=5):
    def lon2str_aux(deg):
        if deg % step == 0:
            dir = 'E'
            if deg < 0:
                dir = 'W'
            return (u"%d\N{DEGREE SIGN} %s") % (np.abs(deg), dir)
        return ''
    return lon2str_aux

m.drawparallels(np.arange(20,80,1),labels=[1,0,0,0],fmt=lat2str(), dashes=[2,2], linewidth=0.5)
m.drawmeridians(np.arange(-20,60,1),labels=[0,0,0,1],fmt=lon2str(), dashes=[2,2], linewidth=0.5)

m.drawparallels(np.arange(20,80,5),labels=[1,0,0,0],fmt=lat2str(), dashes=[2,0], linewidth=0.5)
m.drawmeridians(np.arange(-20,60,5),labels=[0,0,0,1],fmt=lon2str(), dashes=[2,0], linewidth=0.5)

shp_info = m.readshapefile('cities','cities')
x, y = zip(*m.cities)
m.scatter(x,y,15,marker='o',edgecolors='k',color='none',zorder=10)

print m.proj4string

shp_info = m.readshapefile('polygon','sectors',drawbounds=True, color='r')

ax = plt.gca() # get current axes instance
for nshape,seg in enumerate(m.sectors):
    color = "#F9966B"
    poly = Polygon(seg,facecolor=color,edgecolor=color)
    poly.set_alpha(0.75)
    ax.add_patch(poly)

# m.drawlsmask(ocean_color='0.3', lakes=True)
m.fillcontinents(color='0.9', zorder=0)

plt.savefig('008_map_laea.png', dpi=72)
plt.savefig('008_map_laea_big.png', dpi=108)

# create new figure
fig=plt.figure(figsize=(8,5))

# setup oblique mercator basemap.
m = Basemap(projection='cyl',llcrnrlat=35,urcrnrlat=65,\
             llcrnrlon=-10,urcrnrlon=45,resolution='l')

m.drawcountries()
m.drawcoastlines()

m.drawparallels(np.arange(20,80,1),labels=[1,0,0,0],fmt=lat2str(step=10), dashes=[2,2], linewidth=0.5)
m.drawmeridians(np.arange(-20,60,1),labels=[0,0,0,1],fmt=lon2str(step=10), dashes=[2,2], linewidth=0.5)

m.drawparallels(np.arange(20,80,5),labels=[1,0,0,0],fmt=lat2str(step=10), dashes=[2,0], linewidth=0.5)
m.drawmeridians(np.arange(-20,60,5),labels=[0,0,0,1],fmt=lon2str(step=10), dashes=[2,0], linewidth=0.5)

shp_info = m.readshapefile('cities','cities')
x, y = zip(*m.cities)
m.scatter(x,y,15,marker='o',edgecolors='k',color='none',zorder=10)

shp_info = m.readshapefile('polygon','sectors',drawbounds=True, color='r')

ax = plt.gca() # get current axes instance
for nshape,seg in enumerate(m.sectors):
    color = "#F9966B"
    poly = Polygon(seg,facecolor=color,edgecolor=color)
    poly.set_alpha(0.75)
    ax.add_patch(poly)

plt.savefig('008_map_cyl.png', dpi=72)
plt.savefig('008_map_cyl_big.png', dpi=108)

plt.show()

from collections import OrderedDict

#from bokeh.sampledata import us_counties, unemployment
from bokeh.plotting import figure, show, output_notebook, ColumnDataSource
from bokeh.models import HoverTool
import matplotlib.pyplot as plt
from bokeh.io import output_file, show
from pyproj import Proj
import utm
from trebuilding import *
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, 
  Range1d, PanTool, WheelZoomTool, BoxSelectTool)
  
import numpy as np
import geopandas as gpd
lm = gpd.read_file("Lower_manhattan//lower_manhattan.shp")

''' UTM transformation
utm.from_latlon(lat,lon)<->(utm easting,utm northing,18,'T')<-> utm.to_latlon()
UTM Zone 18T
utm.to_latlon(EASTING, NORTHING, ZONE NUMBER, ZONE LETTER).


names=lm.columns.values
Xc=names[73]# Xcoord
Yc=names[74]# YCoord
North=lm[Xc]
East=lm[Yc]

lat1,lon1=utm.to_latlon(East,North,18,'T')


for i in range(len(East)):
	if (East[i]!=0) and (North[i]!=0):
		lat1[i],lon1[i]=utm.to_latlon(East[i],North[i],18,'T')
	else:
		lat1[i]=0
		lon1[i]=0

lm['Ycoord']=lat1
lm['Xcoord']=lon1
'''
#tx.plot(color='blue')

pj = Proj(proj='lcc',datum='NAD83',
	lat_1=40.666667,lat_2=41.033333,lat_0=40.166667,
	lon_0=-74.0,x_0=984250.0,y_0=0.0,ellps='GRS80',
	towgs84=[0,0,0,0,0,0,0],units='us-ft')
	
NAD83 = Proj(init="EPSG:4269")
NYSP1983 = Proj(init="ESRI:102718",preserve_units=True)
	
'''	
PROJCS[
"NAD_1983_StatePlane_New_York_Long_Island_FIPS_3104_Feet",
GEOGCS["GCS_North_American_1983",
DATUM["D_North_American_1983",
SPHEROID["GRS_1980",6378137.0,298.257222101]],
PRIMEM["Greenwich",0.0],
UNIT["Degree",0.0174532925199433]],
PROJECTION["Lambert_Conformal_Conic"],
PARAMETER["False_Easting",984250.0],
PARAMETER["False_Northing",0.0],
PARAMETER["Central_Meridian",-74.0],
PARAMETER["Standard_Parallel_1",40.66666666666666],
PARAMETER["Standard_Parallel_2",41.03333333333333],
PARAMETER["Latitude_Of_Origin",40.16666666666666],
UNIT["Foot_US",0.3048006096012192]]
	'''
	
'''
names=lm.columns.values
Xc=names[73]# Xcoord
Yc=names[74]# YCoord
East=lm[Xc]
North=lm[Yc]

#for i in range(len(East)):
#	lm[Xc][i],lm[Yc][i]=pj( East[i], North[i],inverse=True)

lons,lats=pj( np.array(East), np.array(North),inverse=True)
lm[Xc]=lats
lm[Yc]=lons

#print(lm[Xc].head(),lm[Yc].head())
'''


def gpd_bokeh(df):
    """Convert geometries from geopandas to bokeh format"""
    nan = float('nan')
    lons = []
    lats = []
    for i,shape in enumerate(df.geometry.values):
        if shape.geom_type == 'MultiPolygon':
            gx = []
            gy = []
            ng = len(shape.geoms) - 1
            for j,member in enumerate(shape.geoms):
                xy = np.array(list(member.exterior.coords))
                xs = xy[:,0].tolist()
                ys = xy[:,1].tolist()
                gx.extend(xs)
                gy.extend(ys)
                if j < ng:
                    gx.append(nan)
                    gy.append(nan)
            lons.append(gx)
            lats.append(gy)

        else:     
            xy = np.array(list(shape.exterior.coords))
            xs = xy[:,0].tolist()
            ys = xy[:,1].tolist()
            lons.append(xs)
            lats.append(ys) 

    return lons,lats

east, north = gpd_bokeh(lm)
lons=[]
lats=[]
for i in range(len(east)):
	#xx,yy=pj( np.array(east[i]), np.array(north[i]),inverse=True)
	xx,yy=NYSP1983(np.array(east[i]), np.array(north[i]), inverse=True)
	xx=np.clip(np.array(xx),-85.00,85.0)
	yy=np.clip(np.array(yy),-180.0,180.0)
	if (np.max(xx) < 85.0) and (np.max(yy) < 180.0):  
		lons.append(xx)
		lats.append(yy)

#Latitude: -85 to +85 (actually -85.05115 for some reason)
#Longitude: -180 to +180
#West_Bounding_Coordinate: -74.047751
#East_Bounding_Coordinate: -73.906786
#North_Bounding_Coordinate: 40.879138
#South_Bounding_Coordinate: 40.683884


#print(lons[0],lats[0])


p = figure(title="Lower Manhattan", toolbar_location='left',
          plot_width=700, plot_height=700)
		  
p.patches(lons, lats, fill_alpha=0.5, #fill_color=state_colors,
         line_color="#884444", line_width=2, line_alpha=0.3)

'''
longi=bigbelly['longitude']
lati=bigbelly['latitude']
x=np.zeros(len(lati))
y=np.zeros(len(longi))

for k in range(len(longi)):
	ut=utm.from_latlon(longi[k],lati[k])
	x[k]=ut[0]
	y[k]=ut[1]

print(x[:5])

print(y[:5])
'''
#pj = Proj(proj='utm',zone=18,ellps='WGS84') # use kwargs
#y,x=pj(np.array(lati),np.array(longi))
#x,y=utm.from_latlon( lati,longi)



x=bigbelly['longitude']
y=bigbelly['latitude']
colors=bigbelly['fullness']
times=bigbelly['timestamp']
stream_type=bigbelly['Stream Type']
serial_number=bigbelly['Serial Number']
under_alert=bigbelly['under alert?']

source = ColumnDataSource(
    data=dict(
	lat=y,
	lon=x,
	color=colors
    )
)




circle = Circle(x="lon", y="lat", size=5, 
				fill_color="color", fill_alpha=1.0, line_color=None)

p.add_glyph(source, circle)

output_file('Lower Manhattan.html', title="Lower Manhattan Maps")
show(p)


from bokeh.io import output_file, show
from bokeh.plotting import figure,curdoc,output_file, show
from bokeh.layouts import column
from bokeh.client import push_session
from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Select, Slider
from bokeh.models import CustomJS
from pyproj import Proj
import time
#import datasets
from foottraffic import * #foottraffic
#sfrom trebuilding import * # bigbelly
#from nyclmwifi import *  # Trash

from bokeh.models import (  GMapPlot, GMapOptions, ColumnDataSource, Circle, 
  Range1d, PanTool, WheelZoomTool, BoxSelectTool)
from bokeh.layouts import column
from bokeh.models import CustomJS, ColumnDataSource, Slider
from bokeh.plotting import Figure, output_file, show

import geopandas as gpd
lm = gpd.read_file("Lower_manhattan//lower_manhattan.shp")

#map_options = GMapOptions(lat=40.708076, lng=-74.011085, map_type="roadmap", zoom=15)

#plot = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options)
#plot.title.text = "FootTraffic Lower Manhattan"

# For GMaps to function, Google requires you obtain and enable an API key:
#
#     https://developers.google.com/maps/documentation/javascript/get-api-key
#
# Replace the value below with your personal API key:
#plot.api_key = "AIzaSyB3ysV29bopY3Y6Ifom3DESx0ZLMhnt3Qw"

'''
NAD83 = Proj(init="EPSG:4269")
NYSP1983 = Proj(init="ESRI:102718",preserve_units=True)

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

#
'''

#plot=Figure(plot_width=700, plot_height=700)

#'''
plot = figure(title="Lower Manhattan", toolbar_location='left',
          plot_width=700, plot_height=700,y_range=(40.702, 40.712), x_range=(-74.016, -74.002))
		  
#plot.patches(lons, lats, fill_alpha=0.5, #fill_color=state_colors,
#        line_color="#884444", line_width=2, line_alpha=0.3)

global k
k=0
x1=data_ff[:,0,k]
y1=data_ff[:,1,k]
z1=np.log(data_ff[:,2,k]+1)*2.5

#source=ColumnDataSource(data=dict(x1=x1,y1=y1,z1=z1))
#r=plot.circle(x=x1, y=y1, size=z1,name="excircle",fill_color="red", fill_alpha=0.5,line_color=None)
r=plot.circle(x=x1, y=y1, size=15,name="excircle",fill_color="red", fill_alpha=0.5,line_color=None)

ds=r.data_source
#first time_steps,


def update():
	'''
	i=k
	if (i>=100):
		i=0
	else:
		i=i+1
	'''
	#longi=lons
	#lati=lats
	#xx1=data_ff[:,0,i]+0.01
	#yy1=data_ff[:,1,i]-0.01
	xx1=x1+0.001
	yy1=y1-0.01
	#zz1=np.log(data_ff[:,2,i]+1)*2.5
	#ds.data.update(lons=longi,lats=lati,x1=xx1, y1=yy1,z1=zz1)
	#ds.data.update(x1=xx1, y1=yy1,z1=zz1)
	ds.data.update(x1=xx1, y1=yy1)
	

	



#plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
#slider = Slider(start=0, end=100, value=1, step=1,title="Lower Manhattan")
#layout=column(slider,plot)	

document = curdoc()
document.add_root(plot)
document.add_periodic_callback(update, 100)
#if __name__ == "__main__":
print("\nanimating... press ctrl-C to stop")
session = push_session(document)
output_file("FootTraffic.html")
#show(plot)
session.show()
session.loop_until_closed()
	

#plot.line(x="x1",y= "y1", source=source, line_width=z1[0], line_alpha=0.6)

#x1,y1,z1=data[x1],data['y1'],z1=data['z1']
#z1=np.log(data_ff[:,2,k]+1)*2.5 ;
#source = ColumnDataSource(data=dict(x_coor=data_[:,0,i],y_coor=data_[:,1,i],size=k))

'''
def callback(source=source, window=None):    
	data = source.data    
	k = cb_obj.value    
	x1, y1= data['x1'], data['y1']
	for i in range(len(z1)):
		z1[i]=window.Math.pow(k,1) #np.log(data_ff[:,2,k]+1)*2.5 
	#z1=k	
	source.change.emit()
'''
	

#slider = Slider(start=0, end=100, value=1, step=1,title="Lower Manhattan")#,
                #callback=CustomJS.from_py_func(callback))

#print(z1)
#circle = 
#plot.circle(x="x1", y="y1",source=source, size="z1",fill_color="blue", fill_alpha=0.8)
#plot.add_glyph(source, circle)


'''
layout=column(slider,plot)
curdoc().add_root(layout)	
plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
output_file("FootTraffic.html")
show(layout)
'''
from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Select
from bokeh.models import HoverTool, BoxSelectTool
import pandas as pd
import numpy as np
#from bokeh.models import HoverTool, BoxSelectTool

#from bokeh.models.glyphs import Circle, Line
#import datasets
#from trebuilding import * # bigbelly
#from nyclmwifi import *  # Trash

from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, Line,
  Range1d, PanTool, WheelZoomTool, BoxSelectTool)

map_options = GMapOptions(lat=40.708076, lng=-74.011085, map_type="roadmap", zoom=15)

plot = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options)
plot.title.text = "Meraki Wifi Lower Manhattan"

# For GMaps to function, Google requires you obtain and enable an API key:
#
#     https://developers.google.com/maps/documentation/javascript/get-api-key
#
# Replace the value below with your personal API key:
plot.api_key = "AIzaSyB3ysV29bopY3Y6Ifom3DESx0ZLMhnt3Qw"


id2gismap={
293256: (40.7113543546941, -74.0094307938125), 
289568: (40.7050765042656, -74.0026280883467), 
293812: (40.706621809303, -74.0124751925578), 
263306: (40.7065842614777, -74.0044717490127), 
289702: (40.7046909855223, -74.0023115876829), 
149624924911168: (40.7070877, -74.003546), 
6006960: (40.7063152588123, -74.0060800461652), 
293088: (40.7036091766566, -74.0075137317399), 
208582: (40.7079325116284, -74.0130098463305), 
290340: (40.7029254882542, -74.0095807316538), 
149624923327208: (40.7080646800844, -74.0120860821844), 
290556: (40.7071775511787, -74.0036554634571), 
293148: (40.7079711362727, -74.0094092578875), 
149624923327148: (40.7081643082084, -74.0122899300695), 
149624924913072: (40.7106052777891, -74.0092545747757), 
246656709808192: (40.7112677878556, -74.0092872118112), 
293108: (40.7040252695847, -74.0106010435375), 
289624: (40.7031494313282, -74.0083145495737), 
149624924913904: (40.7080704, -74.0074723), 
149624924909984: (40.7116808059659, -74.0084230899811), 
149624924913952: (40.7088764416627, -74.010618980974), 
208150: (40.7078715146231, -74.0131385923632), 
246656709798000: (40.7113831679251, -74.0091296320315), 
292618: (40.707662064093, -74.0089237512075), 
285396: (40.7040977330852, -74.0077506937087), 
293078: (40.7062419928622, -74.0061085217167), 
289774: (40.7013985338105, -74.0090346336365), 
6008368: (40.707870498068, -74.0117849708258), 
293224: (40.7050844563524, -74.0141049097292), 
15929760: (40.7043698, -74.018091), 
308622: (40.7065201455958, -74.0125610232462), 
149624924910176: (40.703066499116, -74.0104964375496), 
6005680: (40.7082662999098, -74.0112765134472), 
207546: (40.7043867986026, -74.010123074022), 
211954: (40.702457130202, -74.0125799776433), 
6005200: (40.7111596823942, -74.0090532728937), 
6014352: (40.7112989519304, -74.0089312323835), 
286284: (40.7068978593341, -74.0034882724831), 
5276028: (40.7030957501859, -74.0098875761032), 
6009568: (40.7079518273971, -74.0118010640799), 
283328: (40.7033042594045, -74.0063814729911), 
293118: (40.7055582975439, -74.0107438713312), 
289656: (40.7034153968181, -74.0091817975917), 
149624924915616: (37.4180951010362, -122.098531723022), 
205692: (40.70443688648, -74.0100703238568), 
292952: (40.7050224400779, -74.0138997207396), 
246656712525760: (40.7080158825815, -74.0119036919714), 
246656712527232: (40.7079142210024, -74.0119895226599), 
289390: (40.7026906995848, -74.0093779563904), 
278248: (40.7070218883328, -74.0036058425903)
}

#correction
id2gismap[149624924915616]=(40.703943, -74.012356)
id2gismap[310422]=(40.703943, -74.012356)# not correct check later
id2gismap[293028]=(40.703943, -74.012356)# not correct check later

ap_id=list(id2gismap.keys())

latlong=pd.DataFrame.from_dict(id2gismap)
spatial=np.array(latlong)


#first time_steps,
x=spatial[0] # latitude
y=spatial[1] #long 


gm=pd.read_csv('graph_macfull.csv',sep=',',index_col=0)

ap_id=gm.index

edge=gm.values
edge=edge/np.max(edge)
n=len(gm)
diag=np.diagonal(edge)

x=np.zeros(n)
y=np.zeros(n)

for i in range(n):
	x[i],y[i]=id2gismap[ap_id[i]]

	
source = ColumnDataSource(
    data=dict(
		lat=x,
		lon=y,
		apid=ap_id,
		sizes=10*diag
    )
)

hover = HoverTool(tooltips=[
    ("ap_id", "@apid"),
])

#plot.add_tools(hover)

circle = Circle(x="lon", y="lat", size="sizes", 
				fill_color="blue", fill_alpha=1.0, line_color=None)
				
plot.add_glyph(source, circle)

#circle = Line(x="lon",y="lat",line_width="sizes",line_color="red")


source1=ColumnDataSource(
    data=dict(
		vy=x,
		vx=y,
		sizes=diag
    )
)
line = Line(x="vx",y="vy",line_width=1.0,line_alpha=0.5,line_color="red")
plot.add_glyph(source1,line)


'''
for i in range(n):
	for j in range(i):
		ds=ColumnDataSource(
			data=dict(
				lat=np.array([y[i],y[j]]),
				lon=np.array([x[i],x[j]]),
				lw=np.array([edge[i,j]])
			)
		)
	
		line = Line(x="lat",y="lon",line_width="lw",line_color="red")
		plot.add_glyph(ds,line)
'''
		
plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
output_file("Meraki_Wifi.html")
show(plot)
#show(layout)
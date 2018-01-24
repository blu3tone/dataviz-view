from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Select, Slider
from bokeh.models import CustomJS

#import datasets
from foottraffic import * #foottraffic
from trebuilding import * # bigbelly
#from nyclmwifi import *  # Trash

from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, 
  Range1d, PanTool, WheelZoomTool, BoxSelectTool)

map_options = GMapOptions(lat=40.708076, lng=-74.011085, map_type="roadmap", zoom=15)

plot = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options)
plot.title.text = "FootTraffic Lower Manhattan"

# For GMaps to function, Google requires you obtain and enable an API key:
#
#     https://developers.google.com/maps/documentation/javascript/get-api-key
#
# Replace the value below with your personal API key:
plot.api_key = "AIzaSyB3ysV29bopY3Y6Ifom3DESx0ZLMhnt3Qw"

#first time_steps,

data_=data_ff 
i=10
x=data_[:,0,10]
y=data_[:,1,10]
num_pedestrians=np.log(data_[:,2,10])*2.5

source = ColumnDataSource(
    data=dict(
	lat=y,
	lon=x,
	sizes=num_pedestrians
    )
)

update = CustomJS(args=dict(source=source.data), code="""
        var data = source.get('data');
        var k = cb_obj.get('value')
        lon = data['lon']
		lat=data['lat']
		sizes=data['sizes']

		lon=data_[:,0,k]
        lat = data_[:,1,k]
		sizes=np.log(data_[:,2,k])*2.5
        source.trigger('change');
    """)

#slider.on_change('value',update)







circle = Circle(x="lon", y="lat", size="sizes",
				fill_color="red", fill_alpha=0.8, line_color=None)
plot.add_glyph(source, circle)

slider = Slider(start=0, end=100, value=1, step=1, title="Time:",
		callback=update)
layout=column(slider,plot)
curdoc().add_root(layout)	
plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
output_file("FootTraffic_Lower_Manhattan.html")
#show(plot)
show(layout)
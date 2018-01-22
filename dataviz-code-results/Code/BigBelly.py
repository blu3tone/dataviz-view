from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Select

#import datasets
from trebuilding import * # bigbelly
#from nyclmwifi import *  # Trash

from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, 
  Range1d, PanTool, WheelZoomTool, BoxSelectTool)

map_options = GMapOptions(lat=40.708076, lng=-74.011085, map_type="roadmap", zoom=15)

plot = GMapPlot(x_range=Range1d(), y_range=Range1d(), map_options=map_options)
plot.title.text = "BigBelly Lower Manhattan"

# For GMaps to function, Google requires you obtain and enable an API key:
#
#     https://developers.google.com/maps/documentation/javascript/get-api-key
#
# Replace the value below with your personal API key:
plot.api_key = "AIzaSyB3ysV29bopY3Y6Ifom3DESx0ZLMhnt3Qw"

#first time_steps,
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

circle = Circle(x="lon", y="lat", size=10, 
				fill_color="color", fill_alpha=1.0, line_color=None)

plot.add_glyph(source, circle)



	
plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
output_file("BigBelly_Lower_Manhattan.html")
show(plot)
#show(layout)
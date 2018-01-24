from bokeh.io import output_file, show
from bokeh.plotting import figure
from bokeh.layouts import column
from bokeh.io import curdoc
from bokeh.layouts import widgetbox
from bokeh.models.widgets import Select

#import datasets
#from trebuilding import * # bigbelly
from nyclmwifi import *  # Trash

from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, 
  Range1d, PanTool, WheelZoomTool, BoxSelectTool)

names_wifi=wifi.sheet_names

menu = Select(title="Wifi Summary Report:", value=names_wifi[1], options=names_wifi)

sheet=wifi.parse(names_wifi[1])

headers=sheet.columns.values
Name=sheet[headers[0]]
Model=sheet[headers[1]]
Clients=sheet[headers[2]]
Usage=sheet[headers[3]]
p_usage=sheet[headers[4]]


source = ColumnDataSource(
    data=dict(
	client=Clients,
	usage=Usage
    )
)

plot=figure()

circle = Circle(x="client", y="usage", size=10, 
				fill_color="blue", fill_alpha=1.0, line_color=None)

plot.add_glyph(source, circle)


layout=column(menu,plot)
curdoc().add_root(layout)
	
#plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())


output_file("Wifi_Lower_Manhattan.html")
#show(widgetbox(menu))
#show(plot)
show(layout)
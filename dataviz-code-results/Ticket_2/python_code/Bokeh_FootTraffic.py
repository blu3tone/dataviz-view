from bokeh.io import output_file, show
from bokeh.layouts import row,column
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import CheckboxButtonGroup

import numpy as np
import pandas as pd
import os
import glob
import datetime
from pandas.plotting import parallel_coordinates

data=pd.read_csv("foottraffic\\foottraficNovDec2017\\foottrafficNovDec2017.csv")
data=data.iloc[:,1:]

output_file("Mon_Wed.html")

weekday=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
colors=['red','blue','deepskyblue','purple','darkcyan','darkgreen','green']

checkbox_button_group = CheckboxButtonGroup(
        labels=weekday, active=[1,3])

plot = figure(plot_width=1300, plot_height=500,
           title="FootTraffic", toolbar_location="below")

x=np.linspace(0,24,24)

#def callback(active):
#	checkbox_button_group.on_click(callback) 
		
wd=checkbox_button_group.active
#print(wd)


for d in wd:
	dat=data.loc[data['WD']==weekday[d]]
	for i in range(len(dat)):
		plot.line(x,dat.iloc[i,0:24],line_color=colors[d])
		


layout=column(checkbox_button_group,plot)
show(layout)
import numpy as np
import pandas as pd
import os
import glob
import datetime
from pandas.plotting import parallel_coordinates
from pandas.plotting import radviz
from pandas.plotting import andrews_curves
from pandas.plotting import scatter_matrix

import plotly.plotly as py
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go

import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("foottraffic\\foottraficNovDec2017\\foottrafficNovDec2017.csv")

#data=pd.read_csv("foottraffic\\foottraficNovDec2017\\foottraffic2.csv")
data=data.iloc[:,1:]

plt.figure()

#parallel_coordinates(data, 'WD',colormap='gist_rainbow')
#radviz(data,'WD')
#andrews_curves(data, 'WD')
#scatter_matrix(data, alpha=0.5, figsize=(6, 6), diagonal='kde')
#data.plot.box()
#data.plot.area()

hm=data.iloc[:,0:10]
sns.heatmap(hm,cmap='RdYlGn_r', linewidths=0.5, annot=False)

plt.show()

#print(data)

'''
df=pd.read_csv("foottraffic\\foottraffic2.csv")

data = [
    go.Parcoords(
        line = dict(color = df['WD'],
                   colorscale = 'Jet',
                   showscale = True,
                   reversescale = True,
                   cmin = 0,
                   cmax = 100),
        dimensions = list([
            dict(range = [0,4000],
                 constraintrange = [0,4000],
                 label = '0', values = df['0']),
            dict(range = [0,4000],
                 label = '1', values = df['1']),
            dict(range = [0,4000],
                 label = '2', values = df['2']),
            dict(range = [0,4000],
                 label = '3', values = df['3']),
            dict(range = [0,4000],
                 label = '4', values = df['4']),
            dict(range = [0,4000],
                 label = '5', values = df['5']),
            dict(range = [0,4000],
                 label = '6', values = df['6']),
            dict(range = [0,4000],
                 label = '7', values = df['7']),
            dict(range = [0,4000],
                 label = '8', values = df['8']),
            dict(range = [0,4000],
                 label = '9', values = df['9'])
        ])
    )
]

iplot(data, filename = 'parcoords-advanced.html')
'''


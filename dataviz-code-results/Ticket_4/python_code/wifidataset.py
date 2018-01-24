import numpy as np
import pandas as pd
import os
import glob
import datetime
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix
from pandas.plotting import parallel_coordinates
import mpld3
from mpld3 import plugins
from sklearn.preprocessing import LabelEncoder
import matplotlib.animation as animation
# WifiDataSet 

wifi=[]

path =r'C:\\Users\\tvlon\\VizProjects\\wifiDataSet' # use your path
allFiles = glob.glob(path + "/*.csv")

#print(allFiles)
#0 C:\\Users\\tvlon\\VizProjects\\wifiDataSet\Engagement_10312017-12302017.csv
#1 C:\\Users\\tvlon\\VizProjects\\wifiDataSet\Engagement_12282017-12292017.csv
#2 C:\\Users\\tvlon\\VizProjects\\wifiDataSet\LoMa Free WiFi  clients.csv
#3 C:\\Users\\tvlon\\VizProjects\\wifiDataSet\LoMa Free WiFi  clients1day.csv
#4 C:\\Users\\tvlon\\VizProjects\\wifiDataSet\Loyalty_10312017-12302017.csv
#5 C:\\Users\\tvlon\\VizProjects\\wifiDataSet\Loyalty_12282017-12292017.csv
#6 C:\\Users\\tvlon\\VizProjects\\wifiDataSet\Proximity_10312017-12302017.csv
#7 C:\\Users\\tvlon\\VizProjects\\wifiDataSet\Proximity_12282017-12292017.csv

weekday=["Sun","Mon","Tue","Wed","Thu","Fri","Sat"]
colors=['red','blue','deepskyblue','purple','darkcyan','darkgreen','green']

wd_date=pd.read_csv("SummaryReport\\WEEKDAY.csv",index_col=None, header=0)
#print(wd_date)

for file_ in allFiles:
    #print(file_)
    df = pd.read_csv(file_,index_col=None, header=0)
    wifi.append(df)

engagement=wifi[0]
engagement1day=wifi[1]
clients=wifi[2]
clients1day=wifi[3]
loyalty=wifi[4]
loyalty1day=wifi[5]
proximity=wifi[6]
proximity1day=wifi[7] 

eng_names=engagement.columns.values
cli_names=clients.columns.values
loy_names=loyalty.columns.values
pro_names=proximity.columns.values


#Visualization Engagement_12.29.2017-12.29.2017 1 Day
'''
name_e1=engagement1day.columns.values
print(name_e1)
print('engagement1day: ',len(engagement1day))# Scatter with smooth lines and markers

data_e1=engagement1day.loc[:,list(name_e1[3:])]
#print(data_e1.columns.values)

#bar stacked plot
data_e1.plot(marker='o',xticks= np.arange(24))
#data_e1.plot.bar()
#data_e1.plot.bar(stacked=True)
#data_e1.plot.area()
#scatter_matrix(engagement1day.loc[:,list(name_e1[2:])], alpha=0.5, figsize=(6, 6), diagonal='kde')
'''

#Visualization Engagement_10312017-12302017 
'''
print(eng_names)
data_e=engagement.loc[:,list(eng_names[2:])]
parallel_coordinates(data_e, 'WD',colormap='gist_rainbow')

'''

#Visualize Loyalty_12282017-12292017
'''
loy_names=loyalty1day.columns.values
print(loy_names)

data_l1=loyalty1day.loc[:,list(loy_names[3:])]
#print(data_l1.columns.values)

#bar stacked plot
data_l1.plot(marker='o',xticks= np.arange(24))
#data_l1.plot.bar()
#data_l1.plot.bar(stacked=True)
#data_l1.plot.area()
#scatter_matrix(loyalty1day.loc[:,list(loy_names[2:])], alpha=0.5, figsize=(6, 6), diagonal='kde')
'''

#Visualize Loyalty_10312017-12302017
'''
print(loy_names)
print('loyalty: ',len(loyalty))
data_l=loyalty.loc[:,list(loy_names[2:])]
parallel_coordinates(data_l, 'WD',colormap='gist_rainbow')
'''

#Visualize Proximity_12282017-12292017
'''
pro_names=proximity1day.columns.values
print(pro_names)
print('proximity1day: ',len(proximity1day))
data_p1=proximity1day.loc[:,list(pro_names[3:])]
#print(data_p1.columns.values)
#bar stacked plot
#data_p1.plot(marker='o',xticks= np.arange(24))
#data_p1.plot.bar()
#data_p1.plot.bar(stacked=True)
#data_p1.plot.area()
#scatter_matrix(proximity1day.loc[:,list(pro_names[2:])], alpha=0.5, figsize=(6, 6), diagonal='kde')
'''


#Visualize Proximity_10312017-12302017
'''
print(pro_names)
print('proximity: ',len(proximity))
data_p=proximity.loc[:,list(pro_names[2:])]
parallel_coordinates(data_p, 'WD',colormap='gist_rainbow')
'''

#Visualize LoMa Free WiFi  clients1day
'''
print('clients1day: ',len(clients1day))
cli_names=clients1day.columns.values
print(cli_names)

#Convert categorical_to_number
os=clients1day['OS']
categorical_to_number = LabelEncoder()
os_number = categorical_to_number.fit_transform(os)

df=pd.concat([clients1day[cli_names[4]],
	clients1day[cli_names[5]],pd.DataFrame({'OS':os_number}),clients1day[cli_names[7]],pd.DataFrame({'Name':os_number})],axis=1)

print(df.shape)
dfn=(df-df.min())/(df.max()-df.min())

fig, ax = plt.subplots()

df=pd.concat([clients1day[cli_names[4]],
	clients1day[cli_names[5]],pd.DataFrame({'OS':os_number}),clients1day[cli_names[7]]],axis=1)

df=(df-df.min())/(df.max()-df.min())
x=np.array(df)
line, = ax.plot(x[0])

def animate(i):
    line.set_ydata(x[i])  # update the data
    return line,
# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(0, len(df)), init_func=init,
                              interval=50, blit=True)

#parallel_coordinates(dfn, 'Name',colormap='gist_rainbow')
ax.plot([0,0],[0,1])
ax.plot([1,1],[0,1])
ax.plot([2,2],[0,1])
ax.plot([3,3],[0,1])
plt.xticks(np.arange(4),df.columns.values)
'''

#Visualization LoMa Free WiFi _10312017-12302017 Animation

'''
print(cli_names)
print('clients: ',len(clients))

#Convert categorical_to_number
os=clients['OS']
os_number, mapping_index = pd.Series(os).factorize()

clients['OS']=pd.DataFrame({'OS':os_number})

fig, ax = plt.subplots()

df=pd.concat([clients[cli_names[4]],clients[cli_names[5]],
	clients[cli_names[6]],clients[cli_names[7]],clients[cli_names[8]]],axis=1)

df=(df-df.min())/(df.max()-df.min())

x=np.array(df)

line, = ax.plot(x[0])

def animate(i):
    line.set_ydata(x[i])  # update the data
    return line,
# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(0, len(df)), init_func=init,
                              interval=1, blit=True)

#parallel_coordinates(dfn, 'Name',colormap='gist_rainbow')
ax.plot([0,0],[0,1])
ax.plot([1,1],[0,1])
ax.plot([2,2],[0,1])
ax.plot([3,3],[0,1])
ax.plot([4,4],[0,1])

plt.yticks(np.arange(0,1,1/31),wd_date['WD'])
plt.xticks(np.arange(5),df.columns.values)

ani.save('Clients.mp4', fps=30, extra_args=['-vcodec', 'libx264'])
#'''

# Visualization LoMa Free WiFi _10312017-12302017 by day
'''
print(cli_names)
print('clients: ',len(clients))

#Convert categorical_to_number
os=clients['OS']
os_number, mapping_index = pd.Series(os).factorize()

clients['OS']=pd.DataFrame({'OS':os_number})

df=pd.concat([clients[cli_names[4]],clients[cli_names[5]],
	clients[cli_names[6]],clients[cli_names[7]],clients[cli_names[8]]],axis=1)
#Normalization	
df=(df-df.min())/(df.max()-df.min())
dff=pd.concat([df,pd.DataFrame({'Name':os})],axis=1)


d=1/30
df_day=dff[dff['Date']==d]
print(d,": ",len(df_day))
parallel_coordinates(df_day.iloc[:,:], 'Name',colormap='gist_rainbow')
#plt.gca().legend_.remove()
'''

# Visualization Usage Time Series
#'''
print(cli_names)
print('clients: ',len(clients))

x=clients['Usage']
time=clients['Time_h']
#print(max(x))
fig, ax = plt.subplots()
iter=100
line, = ax.plot(x.iloc[0:iter])
def animate(i):
    line.set_ydata(x.iloc[i:i+iter])  # update the data
    #plt.xticks(range(iter),time.iloc[i:i+iter])
    return line,
# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(0, len(x)-iter), init_func=init,
                              interval=25, blit=True)
#'''

plt.show()
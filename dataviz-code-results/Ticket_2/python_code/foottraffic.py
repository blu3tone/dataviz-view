import numpy as np
import pandas as pd
import os
import glob
import datetime
# Data foottraffic 

foottraffic=[]

path =r'C:\\Users\\tvlon\\VizProjects\\foottraffic\\foottraficNovDec2017' # use your path
allFiles = glob.glob(path + "/*.csv")

#print(allFiles)

for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    foottraffic.append(df)


	
#for i in range(len(foottraffic)):

attributes=foottraffic[0].columns.values# 11 attributes

#print(attributes)['hour_beginning' 'location' 'Pedestrians' 'Toward Nassaus St' 
#'Toward Broadway' 'weather_summary' 'temperature' 
#'precipitation' 'lat'  'lon' 'events']
# Locations k
k=0
df=foottraffic[k]

# print location
print(attributes[1],",",df.iloc[k,1])

#starting date and time
print("Started: ",df.iloc[0][0])

num_day=53# from 10/29/2017 to 12/20/2017
#starting date and time
print("Ended: ",df.iloc[num_day*24+23][0])


visistors=np.zeros(shape=(num_day,24))
toward_visistors=np.zeros(shape=(num_day,24))
away_visistors=np.zeros(shape=(num_day,24))

for i in range(num_day):
	for j in range(24):
		visistors[i,j]=df.iloc[i*24+j,2]
		toward_visistors[i,j]=df.iloc[i*24+j,3]
		away_visistors[i,j]=df.iloc[i*24+j,4]

#print(visistors)

np.savetxt('visistor.csv',visistors,delimiter=";")

'''
#dt='10/29/2017'
wday=[];
for i in range(num_day):
	year=2017
	month=
	day=
	dt=datetime.date(year,month,day)
	wd=dt.weekday()
	wday.append(wd)
	
num_weekday=[]
for i in range(7):
	nwd=wday.count(i)
	num_weekday.append(nwd)
	
print(wday)
print(num_weekday)
'''



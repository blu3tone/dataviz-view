import numpy as np
import pandas as pd
import os
import glob
import datetime
import matplotlib.pyplot as plt
import matplotlib
from pandas.plotting import scatter_matrix
from pandas.plotting import parallel_coordinates
import mpld3
from mpld3 import plugins
from sklearn.preprocessing import LabelEncoder
import matplotlib.animation as animation
from pandas.io.json import json_normalize
from datetime import datetime
from matplotlib.widgets import SpanSelector
# WifiMacEventsDataSet 

#wifievent=pd.read_json("sample.json")
wifievent1=pd.read_json("allEvents0.json")
wifievent2=pd.read_json("AllEvents1.json")

wifievent=pd.concat([wifievent1,wifievent2])

wifievent['time_f']=wifievent['time_f']-wifievent['time_f'].min()

'''
convert to timestamp 
b=1513365784.579001
datetime.fromtimestamp(b)
datetime.datetime(2017, 12, 16, 2, 23, 4, 579001)
start: datetime.datetime(2017, 11, 28, 14, 17, 29, 693011)
end: datetime.datetime(2018, 1, 10, 3, 22, 8, 352011)
TIMESTAMP values is '1970-01-01 00:00:01.000000' 
to '2038-01-19 03:14:07.999999'
'''
att=wifievent.columns.values 
#['ap_id', 'cli_key', 'cli_mac', 'cli_name', 'details', 'el_type','time_f'],

'''
att_max=list(ds[0].keys())
att_min=list(ds[0].keys())

for i in idx:
	att=list(ds[i].keys())
	att_min=set(att_min).intersection(att)
	att_max=set(att_max).union(att)
'''
att_min={'channel', 'radio', 'vap'}
att_max={
 'aid',
 'arp_request_failed',
 'arp_request_ip',
 'arp_resp',
 'arp_src',
 'auth_neg_dur',
 'auth_neg_failed',
 'channel',
 'client_mac',
 'dhcp_failed',
 'dns_req_rtt',
 'dns_requests_failed',
 'dns_resp',
 'dns_server',
 'duration',
 'full_conn',
 'http_request_failed',
 'http_request_server',
 'http_resp',
 'instigator',
 'ip_request_failed',
 'ip_request_remote',
 'ip_resp',
 'ip_src',
 'is_wpa',
 'last_auth_ago',
 'multiple_dhcp_servers',
 'radio',
 'reason',
 'rssi',
 'vap'}
#31 attributes

#analysis 
'''
time_f

cli_mac
duration
ip_resp
http_resp
rssi
'''



def TranformDict2DataFrame(wifi):
	ds=wifi['details']
	idx=ds.index
	dfs=pd.DataFrame(columns=att_max)
	for i in idx:
		dfs=dfs.append(pd.Series(ds[i]),ignore_index=True)
	#'ap_id', 'cli_key', 'cli_mac', 'cli_name', 'el_type','time_f'
	dfs['ap_id']=wifi['ap_id']
	dfs['cli_key']=wifi['cli_key']
	dfs['cli_mac']=wifi['cli_mac']
	dfs['cli_name']=wifi['cli_name']
	dfs['el_type']=wifi['el_type']
	dfs['time_f']=wifi['time_f']
	return dfs



ap_id=wifievent[att[0]]
loc_id=ap_id.unique() 
# len(loc_id)=49 position #loc_id[0]=149624924913072
# all elements of wifi for each location id
wifi={}
for id in loc_id:
	wf=wifievent[wifievent[att[0]]==id]
	#wifi.append(wf)
	wifi[id]=wf

df=wifi[292952]

#take a long time for processing
#data=TranformDict2DataFrame(df)

#df=df.sort_values('time_f')# sorted by time_f
#df['time_f']=df['time_f']-df['time_f'].min()	

def ExtractFeatureNaN(data,feature):
	l={}
	n=len(data)
	idx=data.index
	ds=data['details']
	
	for i in range(n):
		key=ds.iloc[i].keys()
		if feature in key:
			x=ds.iloc[i][feature]
			l[idx[i]]=x
	
	return l

#feat="client_mac"
#ft=ExtractFeatureNaN(df,feat)
#dft=pd.DataFrame.from_dict(ft,orient='index')
#for i in range(n):
#    dft.iloc[i,0]=dft.iloc[i,0][:8]
#p=dft.loc[:,0].value_counts()
#p[0:20].plot(kind='bar')



	
def ExtractFeature(data,feature):
	t={}
	l={}
	n=len(data)
	idx=data.index
	ds=data['details']
	
	for i in range(n):
		key=ds.iloc[i].keys()
		if feature in key:
			x=ds.iloc[i][feature]
			tf=data.iloc[i]['time_f']
			l[idx[i]]=x
			t[idx[i]]=tf
	
	dtime=pd.DataFrame.from_dict(t,orient='index')
	ti=dtime.values.astype(np.float)
	dfeat=pd.DataFrame.from_dict(l,orient='index')
	ft=dfeat.values.astype(np.float)	
	
	return [ti,ft]

feat="duration"
t,ft=ExtractFeature(df,feat)

x=np.column_stack((t,ft))
y=x[x[:,0].argsort(kind='mergesort')]

#plt.plot(y[:,0],y[:,1],lw=1.0)
#plt.ylabel('duration')
#plt.xlabel('time')


#sp=np.arange(0,43*24*3600,3600)
#y=np.split(x,sp,axis=0)
#for i in range(len(y)):
#   y[i]=y[i].mean(axis=0)
#y=np.array(y)
#t=y[:,0]
#ft=y[:,1]


#plt.scatter(t,ft,s=1,alpha=1.0,c='b')
	
'''
feature='channel'
cha=ExtractFeature(ds,feature)
feature='radio'
rad=ExtractFeature(ds,feature)
feature='vap'
vap=ExtractFeature(ds,feature)

dfs=pd.DataFrame(columns=['channel','radio','vap'])

dfs['channel']=cha
dfs['radio']=rad
dfs['vap']=vap

dfs['ap_id']=df['ap_id'].values
dfs['cli_key']=df['cli_key'].values
dfs['cli_mac']=df['cli_mac'].values
dfs['cli_name']=df['cli_name'].values
dfs['el_type']=df['el_type'].values
dfs['time_f']=df['time_f'].values

dfs=dfs.sort_values('time_f')# sorted by time_f
dfs['time_f']=df['time_f']-df['time_f'].min()
'''

#plt.show()
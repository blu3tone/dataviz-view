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

#wifievent['time_f']=wifievent['time_f']-wifievent['time_f'].min()

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
ap_id=list(id2gismap.keys())

latlong=pd.DataFrame.from_dict(id2gismap)
spatial=np.array(latlong)
x=spatial[0] # latitude
y=spatial[1] #long 

# location ap_id
#ap_id=wifievent['ap_id']
#time_f=wifievent['time_f']
#cli_mac=wifievent['cli_mac']

#df=wifievent[['ap_id','time_f','cli_mac']]
#df=df.sort_values('time_f')# sorted by time_f

df=wifievent[['ap_id','cli_mac']]

ap_id_dict={}

group_apid=df.groupby('ap_id')
#id=ap_id[0]
#get_id=group_apid.get_group(id)

ap_id=df['ap_id'].unique()
for id in ap_id:
	ap_id_dict[id]=group_apid.get_group(id)

#df[df['ap_id']==id]

num_id=len(ap_id)
graph_id=np.zeros((num_id,num_id))

for i in range(num_id):
	#x=ap_id_dict[ap_id[i]]['cli_mac'].unique()
	x=ap_id_dict[ap_id[i]]['cli_mac']
	graph_id[i,i]=len(x)
	for j in range(i):
		#y=ap_id_dict[ap_id[j]]['cli_mac'].unique()
		y=ap_id_dict[ap_id[j]]['cli_mac']
		z=np.intersect1d(x,y)
		graph_id[i,j]=graph_id[j,i]=len(z)
		

#id=ap_id[0]
#x,y=id2gismap[id]#(40.7106052777891, -74.0092545747757)

#edge=graph_id/np.max(graph_id)

#g=pd.DataFrame(graph_id,columns=ap_id,index=ap_id)
#g.to_csv("graph_macfull.csv",sep=',')
#gm=pd.read_csv('graph_macfull.csv',sep=',',index_col=0)

#reindex
#new_index=range(len(df))
#df.index=new_index

#df['time_f']=pd.to_datetime(df['time_f'], unit='s')
#d.strftime('%Y-%m-%d %H:%M:%S')
#df['ap_id_m']=-1
#df['time_m']=-1

#mac_add=df['cli_mac'].unique()

'''
mac={}
#mac_id=mac_add[0]
for mac_id in mac_add:
	mac_m=df[df['cli_mac']==mac_id]
	mac[mac_id]=mac_m
'''

'''
def MovementOverTime(mac_id):
	#mac1=df[df['cli_mac']==mac_add[0]]#mac_id
	mac1=df[df['cli_mac']==mac_id]
	n=len(mac1)
	idx1=mac1.index
	mac2=mac1['ap_id'].diff()
	mac2.iloc[0]=0.0
	mac3=mac2[mac2!=0.0]
	idx3=mac3.index

	for i in idx3:
		l=idx1.get_loc(i)
		mac1['ap_id_m'].iloc[l-1]=mac1['ap_id'].iloc[l]
		mac1['time_m'].iloc[l-1]=mac1['time_f'].iloc[l]-mac1['time_f'].iloc[l-1]

	mac4=mac1[mac1['time_m']>0.0]	
	return mac4

mac_id=mac_add[0]
mac=MovementOverTime(mac_id)

for i in range(1,len(mac_add)):
	mac_id=mac_add[i]
	mac_t=MovementOverTime(mac_id)
	if len(mac_t)>0:
		mac=pd.concat([mac,mac_t])

mac.to_csv('mac_movement.csv', sep=',')
'''
		
'''
		ap_id        time_f            cli_mac   ap_id_m   time_m
0  293118  1.511853e+09  d4:61:9d:2f:ec:70       0.0  0.00000
1  293118  1.511854e+09  d4:61:9d:2f:ec:70  293108.0  3.58701
2  293108  1.511854e+09  d4:61:9d:2f:ec:70  293118.0  2.11299
3  293118  1.511854e+09  d4:61:9d:2f:ec:70       0.0  0.00000
4  293118  1.511854e+09  d4:61:9d:2f:ec:70       0.0  0.00000
'''


'''
    ap_id                     time_f            cli_mac
0  293118 2017-11-28 07:17:29.693011  d4:61:9d:2f:ec:70
1  293118 2017-11-28 07:18:32.192001  d4:61:9d:2f:ec:70
2  293108 2017-11-28 07:18:35.779011  d4:61:9d:2f:ec:70
3  293118 2017-11-28 07:18:37.892001  d4:61:9d:2f:ec:70
4  293118 2017-11-28 07:19:02.473011  d4:61:9d:2f:ec:70
'''
#apid_u=ap_id.unique() 
# len(loc_id)=49 position #loc_id[0]=149624924913072
# all elements of wifi for each location id
#mac_u=cli_mac.unique()

'''
a=df['time_f'][0]
d=datetime.fromtimestamp(a)
s=d.strftime("%Y-%m-%d %H:%M:%S")
'''

'''
wifi={}
for id in loc_id:
	wf=wifievent[wifievent[att[0]]==id]
	#wifi.append(wf)
	wifi[id]=wf

df=wifi[292952]
'''



#df=df.sort_values('time_f')# sorted by time_f
#df['time_f']=df['time_f']-df['time_f'].min()	

'''
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
'''
	
#feat="client_mac"
#ft=ExtractFeatureNaN(df,feat)
#dft=pd.DataFrame.from_dict(ft,orient='index')
#for i in range(n):
#    dft.iloc[i,0]=dft.iloc[i,0][:8]
#p=dft.loc[:,0].value_counts()
#p[0:20].plot(kind='bar')



'''	
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

'''
	
#feat="duration"
#t,ft=ExtractFeature(df,feat)

#x=np.column_stack((t,ft))
#y=x[x[:,0].argsort(kind='mergesort')]

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
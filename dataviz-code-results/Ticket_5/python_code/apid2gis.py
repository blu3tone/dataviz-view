from meraki import meraki
apikey = "f9a0657c170d0636de51100e0d1656adacd5f9c7"
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import pandas as pd

'''
def ap_id2gis(nameap_id,n2gis):
  ap_id2gismap = dict()
  for i,n in enumerate(nameap_id):
    if i%2 == 0:
      on = n.replace('+',' ')
      ap_id2gismap[nameap_id[i+1]] = n2gis[on]
  return ap_id2gismap

  
myOrgs = meraki.myorgaccess(apikey)
myNetworks = meraki.getnetworklist(apikey,myOrgs[0]['id'])

n2gis=dict([(d['name'],(d['lat'],d['lng'])) \
	for n in myNetworks for d in meraki.getnetworkdevices(apikey,n['id'])])
	
names=[k.replace(' ','+') for k in n2gis]

l = [
    "St+Pauls+roof+02",
    293256,
    "Pier+15+West",
    289568,
    "52+Broadway+north+(UFT)",
    293812,
    "199+Water+(replacement)",
    263306,
    "Pier+15+East",
    289702,
    "Replaces+mr58+@+19+fulton",
    149624924911168,
    "125+Maiden+lane+South",
    6006960,
    "32+Old+Slip+_South+Street+Side",
    293088,
    "Parish+Center+2",
    208582,
    "55+water+East",
    290340,
    "Trinity+indoor+Altar+North",
    149624923327208,
    "Fulton+and+Water+Street",
    290556,
    "West+Gateway",
    293148,
    "Trinity+indoor+Altar+South",
    149624923327148,
    "LP+Broadway+S+Fulton",
    149624924913072,
    "St+Pauls+indoor+02",
    246656709808192,
    "Burger+Burger+(Pearl+St.+Side)",
    293108,
    "Elevated+Acre",
    289624,
    "Blue+Spoon",
    149624924913904,
    "LP+Broadway+and+Vesey",
    149624924909984,
    "LP+Broadway+S+Liberty",
    149624924913952,
    "Parish+Center+1",
    208150,
    "St+Pauls+indoor+01",
    246656709798000,
    "East+Gateway",
    292618,
    "32+Old+Slip_Front+Street+Side",
    285396,
    "125+Maiden+Lane",
    293078,
    "Heli+Port",
    289774,
    "Trinity+steeple+02",
    6008368,
    "11+Broadway+(in+Flatiron+School)",
    293224,
    "Pier+A+Kiosk",
    15929760,
    "52+Broadway+south+(UFT)",
    308622,
    "4+NYP+replacement+6/22/16",
    149624924910176,
    "LP+Broadway+N+of+Trinity",
    6005680,
    "Stone+Street+(East)",
    207546,
    "Whitehall+and+Water+Street+Plaza",
    211954,
    "St+Pauls+roof+01",
    6005200,
    "St+Pauls+roof+03",
    6014352,
    "Fulton+and+Front+Streets",
    286284,
    "Vietnam+Plaza+West",
    5276028,
    "Trinity+steeple+01",
    6009568,
    "Pier+11",
    283328,
    "Burger+Burger+(Stone+Street+Side)",
    293118,
    "Elevated+Acre+Gateway",
    289656,
    "135+John+Street+replacement",
    149624924915616,
    "Stone+Street+(West)",
    205692,
    "Pole+across+from+11+Broadway",
    292952,
    "Trinity+Indoor+rear+North",
    246656712525760,
    "Trinity+Indoor+rear+South",
    246656712527232,
    "55+water+west",
    289390,
    "Light+Up+Front+Street",
    278248
]

id2gismap = ap_id2gis(l,n2gis)
n=len(id2gismap)

id2gismap[149624924915616]=(40.703943, -74.012356)

#40.703943, -74.012356
'''
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


latlong=pd.DataFrame.from_dict(id2gismap)
# position=latlong.iloc[0,i],latlong.iloc[1,i]
spatial=np.array(latlong)

plt.scatter(spatial[0],spatial[1],marker='o')


plt.show()

#print(id2gismap)
'''
df=df.read_json("allEvents0.json")
att=df.columns.values
aid=df[att[0]]
loc=aid.unique()
spatial=[id2gismap[loc[i]] for i in range(len(loc))]

#print(spatial)
first=df[df[att[0]]==loc[0]]# the first location
'''

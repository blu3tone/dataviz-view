from pyproj import Proj
from pyproj import transform

'''	
PROJCS[
"NAD_1983_StatePlane_New_York_Long_Island_FIPS_3104_Feet",
GEOGCS["GCS_North_American_1983",
DATUM["D_North_American_1983",
SPHEROID["GRS_1980",6378137.0,298.257222101]],
PRIMEM["Greenwich",0.0],
UNIT["Degree",0.0174532925199433]],
PROJECTION["Lambert_Conformal_Conic"],
PARAMETER["False_Easting",984250.0],
PARAMETER["False_Northing",0.0],
PARAMETER["Central_Meridian",-74.0],
PARAMETER["Standard_Parallel_1",40.66666666666666],
PARAMETER["Standard_Parallel_2",41.03333333333333],
PARAMETER["Latitude_Of_Origin",40.16666666666666],
UNIT["Foot_US",0.3048006096012192]]
	'''

pj = Proj(proj='lcc',
	datum='NAD83',
	lat_1=40.66666666666667,
	lat_2=41.03333333333333,
	lat_0=40.16666666666667,
	lon_0=-74.0,
	x_0=984250.00000,
	y_0=0.0,
	ellps='GRS80',
	towgs84=[0,0,0,0,0,0,0],
	units='us-ft'	
	)

	
	
p = Proj("+proj=merc +lon_0=0 +k=1 +x_0=0 +y_0=0 +a=6378137 +b=6378137 +towgs84=0,0,0,0,0,0,0 +units=m +no_defs")
	
x = [981106.0]
y = [195544.0]
# return 40.703778, -74.011829
#pj = Proj(proj='utm', zone=18, ellps='WGS84')

'''
Standard_Parallel: 40.666667
Standard_Parallel: 41.033333
Longitude_of_Central_Meridian: -74.000000
Latitude_of_Projection_Origin: 40.166667
False_Easting: 984250.000000
False_Northing: 0.000000
'''

#lon, lat = pj(x, y, inverse=True)

lon, lat = p(x, y, inverse=True)

print(lon, lat)



#inProj = Proj(init='epsg:4269')
#outProj = Proj(init='epsg:2263')
NAD83 = Proj(init="EPSG:4269")
NYSP1983 = Proj(init="ESRI:102718",preserve_units=True)

x1,y1 = 981106.0,195544.0
#x2,y2 = transform(inProj,outProj,x1,y1)
#x2,y2 = transform(NAD83,NYSP1983,x1,y1)

x2,y2=NYSP1983(x1, y1, inverse=True)##### CORRECTED

print ("Test 1: ",x2,y2)

lng,lat= -74.011829,40.703778

x1,y1=transform(NAD83,NYSP1983,lng,lat)
print ("Test 2: ",x1,y1)



'''
 *Generated CRS (+
 proj=lcc +
 lat_1=40.66666666666666 +l
 at_2=41.03333333333333 +
 lat_0=40.16666666666666 +
 lon_0=-74 +
 x_0=300000 +
 y_0=0 +
 ellps=GRS80 +
 towgs84=0,0,0,0,0,0,0 +
 units=us-ft +no_defs)
 '''
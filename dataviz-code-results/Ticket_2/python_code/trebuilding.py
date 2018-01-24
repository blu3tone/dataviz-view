import numpy as np
import pandas as pd

# Data Schemas TRE BUILDING
'''
schemas_3dMap_buildings_new=pd.read_excel(
		'DataSchemas\\3dMap_buildings_new.csv.xlsx')#file 3dMap_buildings_new.csv
print(len(schemas_3dMap_buildings_new))

'''
'''
schemas_ecodev_FerryMasterSheet=pd.ExcelFile(
		'DataSchemas\\ecodev_FerryMasterSheet.xlsx')#multiple sheet ecodev_FerryMasterSheet 

name_FerryMasterSheet=schemas_ecodev_FerryMasterSheet.sheet_names

print(name_FerryMasterSheet)
'''
'''
schemas_ecodev_Private_Ferry_Ridership_CY_2017=pd.read_excel(
		'DataSchemas\\ecodev_Private Ferry Ridership CY 2017.xlsx')
		
print(len(schemas_ecodev_Private_Ferry_Ridership_CY_2017))
'''
'''
schemas_ecodev_Q1_2017_Subway_Ridership=pd.ExcelFile(
		'DataSchemas\\ecodev_Q1 2017 Subway Ridership.xlsx')
name=schemas_ecodev_Q1_2017_Subway_Ridership.sheet_names
print(name)
#'''
'''
schemas_ecodev_StatenIslandFerry_Q1_2017_PASSENGER_COUNTS_CALENDAR_YEAR=pd.read_excel(
	'DataSchemas\\ecodev_StatenIslandFerry_Q1 2017 PASSENGER COUNTS - CALENDAR YEAR.xlsx')

print(len(schemas_ecodev_StatenIslandFerry_Q1_2017_PASSENGER_COUNTS_CALENDAR_YEAR))
'''
#'''
schemas_ops_BigBelly_4_15_14=pd.read_csv(
	'DataSchemas\\ops_BigBelly_4-15-14.csv')
	
bigbelly=schemas_ops_BigBelly_4_15_14

'''
x=bigbelly['longitude']
y=bigbelly['latitude']
colors=bigbelly['fullness']
times=bigbelly['timestamp']
stream_type=bigbelly['Stream Type']
serial_number=bigbelly['Serial Number']
under_alert=bigbelly['under alert?']
'''


#print(list(bigbelly.columns.values))
#print(len(bigbelly))
#print(len(schemas_ops_BigBelly_4_15_14))

#'''
'''
schemas_Ops_Incident_Recap_Data_collected_week_of_June_5th=pd.ExcelFile(
		'DataSchemas\\Ops_Incident Recap Data collected week of June 5th.xlsx')#multiple sheet Ops_Incident Recap Data collected week of June 5th 

name_Ops=schemas_Ops_Incident_Recap_Data_collected_week_of_June_5th.sheet_names

print(name_Ops)
'''

'''
schemas_ops_New_Incident_Recap_Database_Schema=pd.read_excel(
		'DataSchemas\\ops_New Incident Recap Database Schema.xlsx',header=None)
print(len(schemas_ops_New_Incident_Recap_Database_Schema))
#'''

'''
schemas_TRE_Attributes_Sept_2017=pd.read_csv(
		'DataSchemas\\TRE Attributes Sept 2017.csv')
print(len(schemas_TRE_Attributes_Sept_2017))
#'''
'''
schemas_TRE_Attributes=pd.read_csv(
		'DataSchemas\\TRE Attributes.csv')
print(len(schemas_TRE_Attributes))
#'''

'''
schemas_tre_All_Retail_List=pd.read_excel(
		'DataSchemas\\tre_All Retail List.xlsx',header=0)
print(len(schemas_tre_All_Retail_List))
#'''
'''
schemas_tre_RE_Database_Schema=pd.read_excel(
		'DataSchemas\\tre_RE Database Schema.xlsx',header=None)
print(len(schemas_tre_RE_Database_Schema))
'''
'''
schemas_Zum3D_Database_Schema=pd.read_excel(
		'DataSchemas\\Zum3D Database Schema.xlsx',header=None)
print(len(schemas_Zum3D_Database_Schema))
'''





















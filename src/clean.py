#importing pandas to visualise the dataset in tabular format
import pandas as pd
import numpy as np
#introducing stable analysis through random seed
np.random.seed(42)
#importing time function to create animated behaviour
import time
#importing regExp for data cleaning
import re
from numpy import NaN

#seeing the data details manually
def data_detail(daf):
	cols = daf.columns.values
	print ('\nThe training data has {0} rows and {1} columns'.format(daf.shape[0],daf.shape[1]))
	print("\nThe columns in the dataset are :",end="")
	print(cols)
	if daf.duplicated(subset="PRT_ID").sum() == 0:
		print("\nAll ID values are unique.\n")
	print("===========================================================")
	print('\n',daf.info(),'\n')



#data cleaning process in action for AREA column
def data_clean_area(daf):
	print("Data cleaning process in action for AREA column.")
	daf['AREA'].replace('Chrompt', 'Chrompet' ,inplace=True)
	daf['AREA'].replace('Chormpet', 'Chrompet' ,inplace=True)
	daf['AREA'].replace('Chrmpet', 'Chrompet' ,inplace=True)
	
	daf['AREA'].replace('Karapakam', 'Karapakkam' ,inplace=True)
	
	daf['AREA'].replace('KKNagar', 'KK Nagar' ,inplace=True)
	
	daf['AREA'].replace('Velchery', 'Velachery' ,inplace=True)
	
	daf['AREA'].replace('Velchery', 'Velachery' ,inplace=True)
	
	daf['AREA'].replace('Ana Nagar', 'Anna Nagar' ,inplace=True)
	daf['AREA'].replace('Ann Nagar', 'Anna Nagar' ,inplace=True)
	
	daf['AREA'].replace('Adyr', 'Adyar' ,inplace=True)
	
	daf['AREA'].replace('TNagar', 'T Nagar' ,inplace=True)
	return daf


#data cleaning process in action for SALE_COND column
def data_clean_sale_cond(daf):
	print("Data cleaning process in action for SALE_COND column.")
	daf['SALE_COND'].replace('Adj Land', 'AdjLand' ,inplace=True)
	daf['SALE_COND'].replace('Partiall', 'Partial' ,inplace=True)
	daf['SALE_COND'].replace('PartiaLl', 'Partial' ,inplace=True)
	daf['SALE_COND'].replace('Ab Normal', 'AbNormal' ,inplace=True)
	return daf


#data cleaning process in action for PARK_FACIL column
def data_clean_park_facil(daf):
	print("Data cleaning process in action for PARK_FACIL column.")
	daf['PARK_FACIL'].replace('Noo', 'No' ,inplace=True)
	return daf


#data cleaning process in action for BUILDTYPE column
def data_clean_buildtype(daf):
	print("Data cleaning process in action for BUILDTYPE column.")
	daf['BUILDTYPE'].replace('Comercial', 'Commercial' ,inplace=True)
	daf['BUILDTYPE'].replace('Other', 'Others' ,inplace=True)
	daf['BUILDTYPE'].replace('Commercil', 'Commercial' ,inplace=True)
	return daf


#data cleaning process in action for UTILITY_AVAIL column
def data_clean_utility_avail(daf):
	print("Data cleaning process in action for UTILITY_AVAIL column.")
	daf['UTILITY_AVAIL'].replace('All Pub', 'AllPub' ,inplace=True)
	return daf


#data cleaning process in action for STREET column
def data_clean_street(daf):
	print("Data cleaning process in action for STREET column.")
	daf['STREET'].replace('No Access', 'NoAccess' ,inplace=True)
	daf['STREET'].replace('Pavd', 'Paved' ,inplace=True)
	return daf


#grouping all cleaning functions in one
def clean_all(dtf):
	print("Starting data cleaning process for all columns.")
	dtf = data_clean_area(dtf)
	dtf = data_clean_sale_cond(dtf)
	dtf = data_clean_park_facil(dtf)
	dtf = data_clean_buildtype(dtf)
	dtf = data_clean_utility_avail(dtf)
	dtf = data_clean_street(dtf)
	print("Data cleaning complete\n")
	return dtf
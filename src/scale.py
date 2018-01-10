import pandas as pd
import numpy as np
from sklearn.preprocessing import MaxAbsScaler


def scale(df):

	scaler = MaxAbsScaler()

	#scaling data between -1 to 1
	df['INT_SQFT'] = pd.DataFrame(scaler.fit_transform(pd.DataFrame(df['INT_SQFT'])),columns=['INT_SQFT'])
	df['QS_ROOMS'] = pd.DataFrame(scaler.fit_transform(pd.DataFrame(df['QS_ROOMS'])),columns=['QS_ROOMS'])
	df['DIST_MAINROAD'] = pd.DataFrame(scaler.fit_transform(pd.DataFrame(df['DIST_MAINROAD'])),columns=['DIST_MAINROAD'])
	df['QS_BEDROOM'] = pd.DataFrame(scaler.fit_transform(pd.DataFrame(df['QS_BEDROOM'])),columns=['QS_BEDROOM'])
	df['QS_OVERALL'] = pd.DataFrame(scaler.fit_transform(pd.DataFrame(df['QS_OVERALL'])),columns=['QS_OVERALL'])
	df['QS_BATHROOM'] = pd.DataFrame(scaler.fit_transform(pd.DataFrame(df['QS_BATHROOM'])),columns=['QS_BATHROOM'])
	df['REG_FEE'] = pd.DataFrame(scaler.fit_transform(pd.DataFrame(df['REG_FEE'])),columns=['REG_FEE'])
	df['COMMIS'] = pd.DataFrame(scaler.fit_transform(pd.DataFrame(df['COMMIS'])),columns=['COMMIS'])
	df['DATE_DIFF'] = pd.DataFrame(scaler.fit_transform(pd.DataFrame(df['DATE_DIFF'])),columns=['DATE_DIFF'])
	df['YEAR'] = pd.DataFrame(scaler.fit_transform(pd.DataFrame(df['YEAR'])),columns=['YEAR'])

	print("Scaled data:")
	print(df.head())
	print(df.isnull().any())

	return df
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
from sklearn.preprocessing import StandardScaler


def qs_predict(train):
	#making a new dataframe to manipulate the QS columns
	df_qs = train[['QS_ROOMS','QS_BEDROOM','QS_BATHROOM','QS_OVERALL']]
	df_qs.dropna(axis=0,how='any',inplace=True)

	#using Stochastic Gradient Descent to predict QS_OVERALL values for NaN values in dataframe
	from sklearn.linear_model import LinearRegression
	clf_sgd = LinearRegression()
	X = df_qs[['QS_ROOMS','QS_BEDROOM','QS_BATHROOM']]
	y = df_qs['QS_OVERALL']
	X = np.array(X)
	y = np.array(y)
	scaler = StandardScaler()
	scaler.fit(X)
	X = scaler.transform(X)
	clf_sgd.fit(X,y)

	return clf_sgd


def run_qs_predict(df):
	clf = qs_predict(df)
	X = df[['QS_ROOMS','QS_BEDROOM','QS_BATHROOM']]

	scaler = StandardScaler()
	scaler.fit(X)
	X = scaler.transform(X)

	df['QS_OVERALL_NEW'] = clf.predict(X)

	df.loc[df['QS_OVERALL'].isnull(),'QS_OVERALL'] = df['QS_OVERALL_NEW']
	del df['QS_OVERALL_NEW']
	return df
#importing pandas to visualise the dataset in tabular format
import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 150)

import numpy as np
#introducing stable analysis through random seed
np.random.seed(42)
#importing time function to create animated behaviour
import time
#importing regExp for data cleaning
import re
from numpy import NaN

#importing all functions from clean.py
from clean import *

#reading training file
print("Reading training data.")
df = pd.read_csv("../data/train_4aqQp50.csv")

#calling data_details( ) function
data_detail(df)


#calling function to clean data
df = clean_all(df)

#saving the file as cleaned_train.csv
print("Saving file as cleaned_train.csv")
df.to_csv("../data/cleaned_train.csv",index=False)

#Here we are done with the data cleaning process by replacing redundant values with correct paramenter

from basic_predict import *


print("Making new features.\n")
df = make_date_feature(df)
print("\n\nColumns names:",df.columns.values)

print("\nSaving file as feature_train.csv")
df.to_csv("../data/feature_train.csv",index=False)

#Now we need to replace NaN values in QS_OVERALL column

from qs_predict import *
df = run_qs_predict(df)

#removing NaN values in N_ROOMS and N_BATHROOM
df.loc[df['N_BEDROOM'].isnull(),'N_BEDROOM'] = df['N_ROOM'] - df['N_BATHROOM']
df.loc[df['N_BATHROOM'].isnull(),'N_BATHROOM'] = df['N_ROOM'] - df['N_BEDROOM']

#encoding all values
from basic_encoder import *
df = run_encoder(df)

print("\nSaving file as encoded_train.csv")
df.to_csv("../data/encoded_train.csv",index=False)

#scaling all features before training
from scale import *
df = scale(df)

print("\nSaving file as scaled_train.csv")
df.to_csv("../data/scaled_train.csv",index=False)

#=======================================================================
#Done with training data
#Cleaning testing data now

print("Reading test data.")
test = pd.read_csv("../data/test_VJP2kVH.csv")


#calling data_details( ) function
data_detail(test)


#calling function to clean data
test = clean_all(test)

#saving the file as cleaned_test.csv
print("Saving file as cleaned_test.csv")
test.to_csv("../data/cleaned_test.csv",index=False)

#Here we are done with the data cleaning process by replacing redundant values with correct paramenter

from basic_predict import *


print("Making new features.\n")
test = make_date_feature(test)
print("\n\nColumns names:",test.columns.values)

print("\nSaving file as feature_test.csv")
test.to_csv("../data/feature_test.csv",index=False)

#Now we need to replace NaN values in QS_OVERALL column

from qs_predict import *
test = run_qs_predict(test)

#removing NaN values in N_ROOMS and N_BATHROOM
test.loc[test['N_BEDROOM'].isnull(),'N_BEDROOM'] = test['N_ROOM'] - test['N_BATHROOM']
test.loc[test['N_BATHROOM'].isnull(),'N_BATHROOM'] = test['N_ROOM'] - test['N_BEDROOM']

#encoding all values
from basic_encoder import *
test = run_encoder(test)

print("\nSaving file as encoded_test.csv")
test.to_csv("../data/encoded_test.csv",index=False)

#scaling all features
from scale import *
test = scale(test)

print("\nSaving file as scaled_test.csv")
test.to_csv("../data/scaled_test.csv",index=False)

#=================================================================
#Done with cleaning testing data


X_train = df.drop(['PRT_ID','SALES_PRICE'],axis=1)
y_train = df['SALES_PRICE']

X_test = test.drop(['PRT_ID'],axis=1)

'''#using Linear Regression for prediction
from sklearn.linear_model import LinearRegression
clf_reg = LinearRegression()

clf_reg.fit(X_train,y_train)
out_reg = clf_reg.predict(X_test)

output = pd.DataFrame(data = {"PRT_ID":test["PRT_ID"],"SALES_PRICE":out_reg})

print("Writing output file to output_reg.csv")
output.to_csv("../output/output_reg.csv",index=False)


#using Random Forest Regression for prediction
print("Predicting using RandomForest.")
from sklearn.ensemble import RandomForestRegressor
clf_rnd = RandomForestRegressor(n_estimators=20, random_state = 42, verbose=2)

clf_rnd.fit(X_train,y_train)
out_rnd = clf_rnd.predict(X_test)

output = pd.DataFrame(data = {"PRT_ID":test["PRT_ID"],"SALES_PRICE":out_rnd})

print("Writing output file to output_rnd.csv")
output.to_csv("../output/output_rnd.csv",index=False)



#using GradientBoostingRegressor for prediction
print("Predicting using GradientBoost.")
from sklearn.ensemble import GradientBoostingRegressor
clf_gbr = GradientBoostingRegressor(verbose=2,random_state=42)

clf_gbr.fit(X_train,y_train)
out_gbr = clf_gbr.predict(X_test)

output = pd.DataFrame(data = {"PRT_ID":test["PRT_ID"],"SALES_PRICE":out_gbr})

print("Writing output file to output_gbr.csv")
output.to_csv("../output/output_gbr.csv",index=False)



#using AdaBoostRegressor for prediction
print("Predicting using AdaBoostRegressor.")
from sklearn.ensemble import AdaBoostRegressor
clf_abr = AdaBoostRegressor(n_estimators=100, loss='square', random_state=42)

clf_abr.fit(X_train,y_train)
out_abr = clf_abr.predict(X_test)

output = pd.DataFrame(data = {"PRT_ID":test["PRT_ID"],"SALES_PRICE":out_abr})

print("Writing output file to output_abr.csv")
output.to_csv("../output/output_abr.csv",index=False)


#using XGBoost for prediction
import xgboost as xgb

xg_reg = xgb.XGBRegressor(objective="reg:linear", n_estimators=10, seed=123)
xg_reg.fit(X_train, y_train)

preds = xg_reg.predict(X_test)

output = pd.DataFrame(data = {"PRT_ID":test["PRT_ID"],"SALES_PRICE":preds})

print("Writing output file to output_xgb.csv")
output.to_csv("../output/output_xgb.csv",index=False)

#using Linear Regression for prediction
from sklearn.linear_model import LassoCV
alphas = [0.1,0.2,0.3,0.4,0.5,0.01,0.05,1]
clf_reg = LassoCV(alphas=10)

clf_reg.fit(X_train,y_train)
out_reg = clf_reg.predict(X_test)

output = pd.DataFrame(data = {"PRT_ID":test["PRT_ID"],"SALES_PRICE":out_reg})

print("Writing output file to output_lasso_0.1.csv")
output.to_csv("../output/output_lasso_0.1.csv",index=False)
'''
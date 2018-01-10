#importing pandas to visualise the dataset in tabular format
import pandas as pd
import numpy as np
#introducing stable analysis through random seed
np.random.seed(42)
#importing time function to create animated behaviour
import time
import datetime
#importing regExp for data cleaning
import re
from numpy import NaN

'''
    Function date_diff:
        Input -> 1) buy - Buying Date of house
                 2) sell - Selling Date of house       
        Output -> no. of years for which house was held (double value)
'''
def date_diff(df_date):
    buy = df_date.DATE_BUILD
    sell = df_date.DATE_SALE
    buy = datetime.datetime.strptime(buy,"%d-%m-%Y")
    sell = datetime.datetime.strptime(sell,"%d-%m-%Y")
    return (float((sell-buy).days)/365.0)


'''
    Function date_diff:
        Input -> buy - Buying Date of house
        Returns -> year
        Output -> no. of years for which house was held (int value)
'''
def date_year(df_date):
    buy = df_date.DATE_BUILD
    buy = datetime.datetime.strptime(buy,"%d-%m-%Y")
    return (buy.year)
    

def make_date_feature(daf):
	daf['DATE_DIFF'] = daf.apply(date_diff,axis=1)
	daf['YEAR'] = daf.apply(date_year,axis=1)
	daf.drop(columns=['DATE_SALE', 'DATE_BUILD'], inplace=True)
	print(daf.head(10))
	return daf

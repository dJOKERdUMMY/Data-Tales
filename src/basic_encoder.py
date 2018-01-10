import pandas as pd
import numpy as np

#encoding data
#Define a generic function using Pandas replace function
def coding(col, codeDict):
  colCoded = pd.Series(col, copy=True)
  for key, value in codeDict.items():
    colCoded.replace(key, value, inplace=True)
  return colCoded
 
def run_encoder(df):
    #Coding LoanStatus as Y=1, N=0:
    df["AREA"] = coding(df["AREA"], {
        'Chrompet':0,
        'Karapakkam':1,
        'KK Nagar':2,
        'Velachery':3,
        'Anna Nagar':-3,
        'Adyar':-2,
        'T Nagar':-1})

    df["SALE_COND"] = coding(df["SALE_COND"], {
        'AdjLand':0,
        'Partial':1,
        'Normal Sale':2,
        'AbNormal':-2,
        'Family':-1})

    df['PARK_FACIL'] = coding(df['PARK_FACIL'],{
        'Yes':1,
        'No':0})

    df['BUILDTYPE'] = coding(df['BUILDTYPE'],{
        'House':0,
        'Others':1,
        'Commercial':-1})

    df['UTILITY_AVAIL'] = coding(df['UTILITY_AVAIL'],{
        'ELO':-1,
        'NoSewr ':-2,
        'NoSeWa':0,
        'AllPub':1})

    df['STREET'] = coding(df['STREET'],{
        'Paved':1,
        'Gravel':0,
        'NoAccess':-1})

    df['MZZONE'] = coding(df['MZZONE'],{
        'RL':1,
        'RH':2,
        'RM':3,
        'C':0,
        'A':-1,
        'I':-2
        })

    return df
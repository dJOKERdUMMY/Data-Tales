#ignore this piece of code
#it was thought to be used in the model but was later removed because of redundant issues

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

from pred import *
from qs_predict import *

df = pd.read_csv("train.csv")


clf = qs_predict(df)



'''print(clf.predict(row['QS_ROOMS','QS_BEDROOM','QS_BATHROOM']))'''

'''df['QS_OVERALL'] = df.apply(remove_na_fares, axis=1)'''

X = df[['QS_ROOMS','QS_BEDROOM','QS_BATHROOM']]

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

df['QS_OVERALL_NEW'] = clf.predict(X)

df.loc[df['QS_OVERALL'].isnull(),'QS_OVERALL'] = df['QS_OVERALL_NEW']

print(df.head(90))

'''
print(out.value_counts(dropna=False))

for i in range(len(df.QS_OVERALL)):
	if(pd.isnull(df['QS_OVERALL'].iloc[i])):
		df['QS_OVERALL'].iloc[i] = out.iloc[i]

print(out.value_counts(dropna=False))

diff = '''
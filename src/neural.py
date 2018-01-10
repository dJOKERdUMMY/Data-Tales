#the less hidden layes didn't work out as per the graph above so using more hidden layers
#as per above diagram using only adam and nadam
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

import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

from keras.callbacks import EarlyStopping
early_stopping_monitor = EarlyStopping(patience=80)

df = pd.read_csv("../data/scaled_train.csv")
test = pd.read_csv("../data/scaled_test.csv")

X_train = df.drop(['PRT_ID','SALES_PRICE'],axis=1)
y_train = df['SALES_PRICE']

X_test = test.drop(['PRT_ID'],axis=1)

# Import necessary modules
import keras
from keras.layers import Dense
from keras.models import Sequential

# Specify the model
predictors = X_train.values
target = y_train.values.reshape((-1,1)).astype('int32')

n_cols = predictors.shape[1]

#model 1
model11 = Sequential()
model11.add(Dense(100, activation='relu', input_shape=(n_cols,)))
model11.add(Dense(70, kernel_initializer='normal', activation='relu'))
model11.add(Dense(50, kernel_initializer='normal', activation='relu'))
model11.add(Dense(32, kernel_initializer='normal', activation='relu'))
model11.add(Dense(1, kernel_initializer='normal'))

#model 2
model22 = Sequential()
model22.add(Dense(100, activation='relu', input_shape=(n_cols,)))
model22.add(Dense(70, kernel_initializer='normal', activation='relu'))
model22.add(Dense(50, kernel_initializer='normal', activation='relu'))
model22.add(Dense(32, kernel_initializer='normal', activation='relu'))
model22.add(Dense(1, kernel_initializer='normal'))

# Compile model
model11.compile(loss='mean_squared_error', optimizer='nadam')
print("model11 loss:",model11.loss)

# Compile model
model22.compile(loss='mean_squared_error', optimizer='adam')
print

model_train11 = model11.fit(predictors,target, epochs=800, validation_split=0.4, callbacks=[early_stopping_monitor], verbose=True)
model_train11

model_train22 = model22.fit(predictors,target, epochs=800, validation_split=0.4, callbacks=[early_stopping_monitor], verbose=True)
model_train22


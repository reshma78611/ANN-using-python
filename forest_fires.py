# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lakrtC5NCj-AH7_o1ySpVT3Seb9DEMN4
"""

import numpy as np
import pandas as pd

from google.colab import files
upload=files.upload()

forest=pd.read_csv('forestfires.csv')
forest.head()

forest.pop('month')
forest.head()

forest.pop('day')
forest.head()

forest.isna().sum()

from sklearn import preprocessing
label_encoder=preprocessing.LabelEncoder()
forest['size_category']=label_encoder.fit_transform(forest['size_category'])

forest.head()

x=forest.iloc[:,0:28]
y=forest.iloc[:,28]

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
x_train=sc.fit_transform(x_train)
x_test=sc.fit_transform(x_test)


#Neural Network - ANN
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

#initializing ANN
model=Sequential()

#adding input and 1st hidden layer
model.add(Dense(units=10,activation='relu',kernel_initializer='he_uniform',input_dim=28))
#adding 2nd hidden layer
model.add(Dense(units=8,activation='relu',kernel_initializer='he_uniform'))
#adding output layer
model.add(Dense(units=1,kernel_initializer='glorot_uniform',activation='sigmoid'))


#compile the model
model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

#fit the model
model.fit(x_train,y_train,batch_size=10,epochs=150,validation_split=0.33)

y_pred=model.predict(x_test)

y_pred


#evaluating the model
scores = model.evaluate(x_test, y_test)
print("%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))
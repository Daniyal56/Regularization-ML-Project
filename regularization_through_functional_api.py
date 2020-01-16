# -*- coding: utf-8 -*-
"""Regularization through Functional API.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1mntXOALuCMGwxWJieuSTJf99OnXyt_g1
"""

# Baseline Model on the Sonar Dataset
import numpy
import keras
from pandas import read_csv
from keras.models import Sequential
from keras.layers import Dense
from keras import regularizers
from keras.utils import to_categorical
from keras import optimizers
from keras.optimizers import SGD

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)
# load dataset
dataframe = read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/undocumented/connectionist-bench/sonar/sonar.all-data ", header=None)
dataset = dataframe.values
# split into input (X) and output (Y) variables
X = dataset[:,0:60].astype(float)
Y = dataset[:,60]

# encode class values as integers
dataframe[60] = [0 if x == 'R' else 1 for x in dataframe[60]]
encoded_Y = dataframe[60]
Y = to_categorical(encoded_Y)

inputs = keras.Input(shape=(60,))
x = Dense(60, activation='relu')(inputs)
x = Dense(30, activation='relu')(x)
outputs = Dense(2, activation='sigmoid')(x)

#creating model

model = keras.Model(inputs,outputs)

# Compile model
sgd = SGD(lr=0.01, momentum=0.8, decay=0.0, nesterov=False)
model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])

model.fit(X,Y,epochs=300)

# Smaller Network
# create model
inputs = keras.Input(shape=(60,))
x = Dense(48, activation='relu')(inputs)
x = Dense(13, activation='relu')(x)
outputs = Dense(2, activation='relu')(x)
model = keras.Model(inputs,outputs)
# Compile model
sgd = SGD(lr=0.01, momentum=0.8, decay=0.0, nesterov=False)
model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])
model.fit(X,Y,epochs=300)

# Overfitting
# create model
inputs = inputs = keras.Input(shape=(60,))
x = Dense(512,kernel_regularizer=regularizers.l2(0.1),activity_regularizer=regularizers.l1(0.1), activation='relu')(inputs)
x = Dense(64,  activation='relu')(x)
x= Dense(32,   activation='relu')(x)
x= Dense(18,  activation='relu')(x)
outputs= Dense(2,  activation='sigmoid')(x)
model = keras.Model(inputs,outputs)
# Compile model
sgd = SGD(lr=0.1, momentum=0.8, decay=0.0, nesterov=False)
model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])
model.fit(X,Y,epochs=1000)

# Tunning
# create model
inputs = keras.Input(shape=(60,))
x = Dense(30,  kernel_regularizer=regularizers.l2(0.01),activity_regularizer=regularizers.l1(0.01), activation='relu')(inputs)
x = Dense(18, activation='relu')(x)
outputs = Dense(2, activation='sigmoid')(x)

model = keras.Model(inputs,outputs)
# Compile model
sgd = SGD(lr=0.01, momentum=0.8, decay=0.0, nesterov=False)
model.compile(loss='binary_crossentropy', optimizer=sgd, metrics=['accuracy'])
model.fit(X,Y,epochs=300)




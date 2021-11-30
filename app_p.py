# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 09:53:34 2021

@author: EliteBook
"""

import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error, accuracy_score
loaded_model = pickle.load(open('C:/Users/EliteBook/Desktop/stack/AIAssignment/trained_model.sav', 'rb'))
Xtest = pd.read_pickle('C:/Users/EliteBook/Desktop/stack/AIAssignment/d.file')
Ytest = pd.read_pickle('C:/Users/EliteBook/Desktop/stack/AIAssignment/dy.file')
predict_from_load = loaded_model.predict(Xtest)
#print(predict_from_load)
print(Ytest)
#print(len(predict_from_load))
#print(len(Ytest))
#r2_score(Ytest, predict_from_load)
#mean_absolute_error(Ytest, predict_from_load)
#mean_squared_error(Ytest, predict_from_load)
#np.sqrt(mean_squared_error(Ytest, predict_from_load))
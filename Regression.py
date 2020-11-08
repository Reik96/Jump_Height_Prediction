# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 23:08:43 2020

@author: rsele
"""


import pandas as pd
import numpy as np
import pickle
import datetime
from datetime import date

from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV

data = pd.read_excel(r"C:\Users\...")


def from_dob_to_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

data["age"]=data["Birthdate"].apply(lambda x: from_dob_to_age(x))

y_spike = data["Spike"]


y_block = data["Block"]

data=data.drop(labels=["Team","Name","Birthdate"],axis="columns")

X = data[["Height","Weight","age"]]



regressor_spike = Lasso()


regressor_block = Lasso()

params={"alpha":[0.01,0.02,0.05,0.1,0.5,1,5,10,100,200,500,1000]}



regressor_spike = GridSearchCV(regressor_spike,params)
regressor_spike.fit(X,y_spike)

print(regressor_spike.best_params_)
regressor_block= GridSearchCV(regressor_block,params)
regressor_block.fit(X,y_block)



# Saving model to disk
pickle.dump(regressor_spike, open('model_spike.pkl','wb'))
pickle.dump(regressor_block, open('model_block.pkl','wb'))



# Loading model to compare the results
model_spike = pickle.load(open('model_spike.pkl','rb'))
model_block = pickle.load(open('model_block.pkl','rb'))

print(model_spike.predict([[208,99,29]]))
print(model_block.predict([[208,99,29]]))

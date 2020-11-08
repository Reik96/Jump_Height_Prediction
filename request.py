# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 23:57:35 2020

@author: rsele
"""
import requests

url = 'http://localhost:5000/predict'
r = requests.post(url,json={"height":0, "weight":0, "age":0})

url1 = 'http://localhost:5000/predict'
r1 = requests.post(url1,json={"height":0, "weight":0, "age":0})

print(r.json())
print(r1.json())
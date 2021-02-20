# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:11:29 2021

@author: kurtulusocL
"""

import numpy as np
sayilar=np.array([0,5,10,15,20,25,30])
print(sayilar[0])
print(sayilar[4])
print(sayilar[0:3])

sayilar2=np.array([[1,3,5],[7,21,35]])
print(sayilar2[0])
print(sayilar2[:,2])
print(sayilar2[0,2])
print(sayilar2[:,0:2])

for row in sayilar:
    print([row])
    
for row in sayilar2:
    print([row])

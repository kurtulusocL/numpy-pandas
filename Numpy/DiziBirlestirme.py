# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:51:48 2021

@author: kurtulusocL
"""

import numpy as np

a=np.floor(10*np.random.random((2,3)))
print(a)
b=np.floor(10*np.random.random((2,3)))
print(b)

c=np.vstack((a,b)) #yatay
print(c)
d=np.hstack((a,b)) #dikey
print(d)
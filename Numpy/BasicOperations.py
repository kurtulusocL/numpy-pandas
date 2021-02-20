# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 19:58:24 2021

@author: kurtulusocL
"""

import numpy as np
a=np.array([20,30,40,50])
b=np.arange(4)
c=a-b
print(a)
print(b)
print(c)

e=10*np.sin(a)
print(e<7)
print(a*b)
print(a@b) #matris çarpımı
print(a.dot(b)) #matris çarpımı

x=np.ones((2,4))
y=np.zeros((2,4))
print(x)
print(y)
print(np.sum(b))

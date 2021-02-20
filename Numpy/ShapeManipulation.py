# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 20:42:23 2021

@author: kurtulusocL
"""

import numpy as np
a=np.floor(10*np.random.random((3,4)))
print(a)

print(a.shape)
print(a.ravel())

a=a.ravel()
print(a)
print(a.shape)
print(a.reshape(2,6))

a=a.reshape(3,4)
a=a.reshape(6,2)
print(a.T)
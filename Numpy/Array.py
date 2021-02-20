# -*- coding: utf-8 -*-
import numpy as np

a= np.arange(1,10)
print(a)

a=np.array([1,3,5,7,9,11])
print(a)
print(a.dtype)
r=a.reshape(2,3)
print(r)

a=np.array([1.01,3,5,7,9,11])
print(a.dtype)

b=np.array([[1,3],[10,20],[9,11]])
print(b)
print(b.ndim)
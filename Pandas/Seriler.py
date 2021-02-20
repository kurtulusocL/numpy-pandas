# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 22:11:38 2021

@author: kurtulusocL
"""
import pandas as pd
import numpy as np

data=np.array(["Alin","Ahmet","Mehmet"])
s=pd.Series(data)
s=pd.Series(data, index=[1,2,3])
print(s)

data2={"matematik":10,"fizik":20,"beden eğitimi":99}
s2=pd.Series(data2)
print(s2)
print(s2["fizik"])


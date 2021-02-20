# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 22:26:01 2021

@author: kurtulusocL
"""

import pandas as pd
import numpy as np

data=[10,20,30,40,50]
df=pd.DataFrame(data)
print(df)

data2=[["Ali",21,"Ankara"],["Veli",31,"İzmir"],["Ayşe",27,"Aydın"]]
df2=pd.DataFrame(data2,columns=["İsim","Yaş","Şehir"])
print(df2)

data3={"İsim":["Ali","Veli","Ayşe"],"Yaş":[21,31,27],"Şehir":["Ankara","İzmir","Aydın"]}
df3=pd.DataFrame(data2,columns=["İsim","Yaş","Şehir"])
print(df3)
print(df3["İsim"], df3["Şehir"])

#del df3["Şehir"]
df3.pop("Şehir")
print(df3)

print(df3.loc[2])
print(df3.iloc[1]

df4 = df3.append(df2)
print(df4)
print(df4.head()) #baştaki 5 data
print(df4.tail()) #sondaki 5 data

print(df4["İsim"],df4["Yaş"])
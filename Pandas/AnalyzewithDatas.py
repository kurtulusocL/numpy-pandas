# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 20:18:28 2021

@author: kurtulusocL
"""

import pandas as pd
notlar = pd.read_csv("grades.csv")
df=notlar
print(df)
notlar.columns=["İsim","Soyisim","SSN","Test1","Test2","Test3","Test4","Final","Sonuc"]
print(notlar["Sonuc"])
print(notlar["Final"])
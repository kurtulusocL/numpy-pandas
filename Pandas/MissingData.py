# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 21:55:55 2021

@author: kurtulusocL
"""
import pandas as pd

url="http://bit.ly/uforeports"
data=pd.read_csv(url)
print(data)

print(data.columns)
print(data.head())
print(data[["City","State","Time","Shape Reported","Colors Reported"]].head(100))
print(data.isnull().head(100))
print(data.notnull().head(100))
print(data.isnull().groupby("City").State.sum())
print(data[data.City.isnull()])
print(data[data.City.notnull()])


print(data.shape)
data=data.dropna(how="all")

data=data.dropna(subset=["City","Colors Reported"],how="any")
print(data.shape)

print(data["Shape Reported"].value_counts(dropna=False))
data["Shape Reported"].fillna(value="Belirsiz",inplace=True) #boş veriyi doldur ve belirsiz olarak değiştir ve kaydet
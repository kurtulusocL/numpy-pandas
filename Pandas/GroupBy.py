# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 21:28:48 2021
@author: kurtulusocL
"""

import pandas as pd
imdb=pd.read_csv("imdb-1000.csv")
print(imdb.columns)
print(imdb)

print(imdb.star_rating.mean())
print(imdb.groupby("genre").star_rating.mean())

print(imdb=imdb.drop("content_rating",axis=1)) #1: kolon, 0: satır, content_rating kolonunu uçurduk
print(imdb)
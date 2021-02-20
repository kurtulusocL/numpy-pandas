# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 21:04:25 2021
@author: kurtulusocL
"""

import pandas as pd
imdb=pd.read_csv("imdb-1000.csv")
print(imdb)
print(imdb.columns)
print(imdb.head())
print(imdb.tail())
print(imdb["title"].head())
print(imdb[["title","star_rating","content_rating"]].head())
print(imdb[:9][["title","star_rating"]])

print(imdb[imdb["star_rating"]>=8.7][["title","star_rating"]])
print(imdb[
        (imdb["star_rating"]>=8.7)
        &
        (imdb["star_rating"]<=9.0)]
[["title","star_rating"]])

print(imdb[
        (imdb["star_rating"]>=9.5)
        |
        (imdb["star_rating"]<=7.6)]
[["title","star_rating"]])

print(imdb.query("star_rating>=9.0")[["title","star_rating"]])
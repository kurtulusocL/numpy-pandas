# -*- coding: utf-8 -*-

import pandas as pd
data=pd.read_table("orders.tsv")

print(data.columns)
print(data.head(20))

data.sort_values('item_name')
data.sort_values("item_price",ascending=False)

data.sort_values(["item_name","item_price"], ascending=False)

data1 = {
       "id":[1,2,3,4],
       "ad":["Ali","Ayşe","Mehmet","Veli"],
       "soyad":["Ok","Merve","Salih","Deli"]
       }

data2 = {
        "id":[1,3,4,7],
       "ad":["Eyüp","Ahmet","Cemal","Hatice"],
       "soyad":["Ok","Merve","Salih","Deli"]
        }

data1df=pd.DataFrame(data1)
data2df=pd.DataFrame(data2)
print(data1df)
print(data2df)


print(pd.merge(data1df,data2df,on="id",how="inner"))
print(pd.merge(data1df,data2df,on="id",how="left"))
print(pd.merge(data1df,data2df,on="id",how="right"))

print(pd.concat([data1df,data2df]))
print(pd.concat([data1df,data2df],axis=1))

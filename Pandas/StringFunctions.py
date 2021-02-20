# -*- coding: utf-8 -*-

import pandas as pd

orders=pd.read_table("orders.tsv")
print(orders.columns)
print(orders.head(20))


print(orders.item_name.str.upper())
orders.item_name=orders.item_name.str.upper()
print(orders.item_name)
print(orders.item_name.str.contains("Chicken".upper()))

orders.choice_description=orders.choice_description.str.replace("[","")
orders.choice_description=orders.choice_description.str.replace("]","")

orders.choice_description=orders.choice_description.str.replace("[","").replace("]","")
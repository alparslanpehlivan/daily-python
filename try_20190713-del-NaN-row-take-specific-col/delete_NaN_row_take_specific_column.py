import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

df = pd.read_excel('k.xlsx', sheet_name='Sheet1')
print(df.head(5))

#print(df.loc[:,["Unnamed: 5","Unnamed: 33","Unnamed: 34","Unnamed: 35"]])
df=df[~df['Unnamed: 33'].isnull()]
print(df)
df1 = df[["Unnamed: 5","Unnamed: 33","Unnamed: 34","Unnamed: 35"]]
print(df1)

 

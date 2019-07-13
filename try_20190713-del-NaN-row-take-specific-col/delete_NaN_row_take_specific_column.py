import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

df = pd.read_excel('CAETeam.xlsx', sheet_name='Terminplan 2019')
print(df.head(5))

#print(df.loc[:,["Unnamed: 5","Unnamed: 33","Unnamed: 34","Unnamed: 35"]])
df=df[~df['Unnamed: 33'].isnull()]
print(df)
df1 = df[["Unnamed: 5","Unnamed: 33","Unnamed: 34","Unnamed: 35"]]
print(df1)

#print(df.loc[['AGB Box Evaluation','PP2020']])
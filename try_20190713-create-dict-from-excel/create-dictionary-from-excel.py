import pandas as pd
from openpyxl import load_workbook
from openpyxl.styles import PatternFill, colors, Fill

my_dic = pd.read_excel('k.xlsx', index_col=0).to_dict()

#sheet_data = pd.read_csv('k.xlsx')
#sheet_data = sheet_data[['Alparslan', 'value 2']]

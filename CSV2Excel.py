''' Project : Convert CSV File into Excel File  '''

'''  
- Basic Setup -

# pip install pandas 
# pip install openpyxl  (Python Library for Read/Write Excel Files)

'''
import pandas as pd
from openpyxl import Workbook

# Reading a CSV File
read_file = pd.read_csv(r'dataset.csv')

# saving or writing a xlsx file
write_file = pd.ExcelWriter(r'data.xlsx')

# Convert CSV into Excel File
read_file.to_excel(write_file, index = False, header=True, sheet_name="Sheet1")

write_file.save()

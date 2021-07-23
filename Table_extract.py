import pandas as pd
import camelot

def table_extract(filename = 'test.pdf'):
    tables = camelot.read_pdf(filename, flavor='stream')
    table_df = tables[0].df
    return table_df

def save_table(table_df,table_num):
    datatoexcel = pd.ExcelWriter('table.xlsx')
    table_df.to_excel(datatoexcel,sheet_name='table'+str(table_num))
    datatoexcel.save()
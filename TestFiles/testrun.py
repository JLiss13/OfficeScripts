#Created by Jordan Liss
#Extract pages from .PDF into current directory
import os
import xlsxwriter
# Write to excel spreadsheet
Curr_Con_directory='M:\Engineering\Current_Configuration\MTS_Rails' 
hyperlinkswb='hyperlinks.xlsx'
hyperlinkswb_path=os.path.join(Curr_Con_directory,hyperlinkswb) # Make hyperlink sheet path
workbook=xlsxwriter.Workbook(hyperlinkswb_path)
worksheet=workbook.add_worksheet('Curr_Con Hyperlinks')
url_format=workbook.add_format({'font_color': 'blue','underline':1})
Column='A'
Row=3
location=Column+str(Row)
worksheet.write_url(location,hyperlinkswb_path,url_format,'NewFilename')
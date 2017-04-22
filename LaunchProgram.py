import os
# If using a Mac
# os.system("open /Applications/Chess.app") # open program
os.system("open /Users/Jaliss/Dropbox/Electricore_Dropbox/Task5/ESCT/Energy_Storage_Computational_Tool_Version_1.2.xlsm") #open a file

# If using a windows
from win32com.client import Dispatch
xl = Dispatch('Excel.Application')
wb = xl.Workbooks.Open('C:\\Documents and Settings\\GradeBook.xls')
xl.Visible = True    # optional: if you want to see the spreadsheet


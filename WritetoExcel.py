# Create .csv file in the current configuration folder that has hyperlinks with file characteristics (hyperlink name,main category, sub category, drawing No.)
# Written by Jordan Liss
import os
import csv
# Read csv file using numpy
Curr_Con_directory='M:\Engineering\Current_Configuration\MTS_Rails' 
hyperlinksfile='hyperlinks.csv'
hyperlinksfile_path=os.path.join(Curr_Con_directory,hyperlinksfile) # Make hyperlink sheet path
fileopen=open(hyperlinksfile_path,'rb')
reader=csv.reader(fileopen,delimiter=',')
array=np.array(reader)
# Read csv file using panda
array= pandas.read_csv(hyperlinksfile_path)
#close the fileopen after extracting array data
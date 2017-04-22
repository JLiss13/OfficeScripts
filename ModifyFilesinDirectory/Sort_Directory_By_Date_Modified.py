#For write hyperlinks in a directory to a .csv or .txt
import os 
import numpy
Folderpath=raw_input('Destination Folderpath?')
Name=raw_input('Common name found in title? (Plus any underscores or blanks after)')
FilestobeChanged=input("What is the last file number that needs to be changed?")
# Name="TP Sub SD-LRT-8_"
hyperlink_directory='M:\Engineering\Current_Configuration\MTS_Rails\hyperlinks.csv'
Files=os.listdir(Folderpath)
filenum=0
# Obtain Date Modified Time Stamp
Date_Modified=numpy.zeros(len(Files))
while filenum <len(Files):
    filepath=os.path.join(Folderpath,Files[filenum])
    Date_Modified[filenum]=os.path.getmtime(filepath)
    print Date_Modified[filenum], filepath
    filenum=filenum+1
#Sort the Files Array into a new array called NewFiles grabbing only
#date modified times from october on
Date_Modified_Index=[i for i,v in enumerate(Date_Modified>1.41230e9)if v]
NewFiles=['']*len(Date_Modified_Index)
filenum=0
while filenum < len(Date_Modified_Index):
    NewFiles[filenum]=Files[Date_Modified_Index[filenum]]
    filenum=filenum+1
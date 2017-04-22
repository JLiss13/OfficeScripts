#Created by Jordan Liss
#Read drawings as Tiffs to extract information and
#organize their PDF counterparts into their respective folders.
#KNOW THE SCAN RESOLUTION BEFORE STARTING

#Pre-Code Execution Setup 
#1) Convert Comprehensive PDF into individual tiff files
#2) Place tesseract, pytesser in the same folder as tiffs
#3) Run code
#4) Check hyperlink.csv


import os
from PIL import Image
from pytesser import *
import numpy
import cv
import matplotlib.pyplot as plt
from pyPdf import PdfFileWriter, PdfFileReader
from CurCon_Module import ExtractFileCategories, PrintToCSVReport, imagegrab

clear=lambda: os.system('cls') # clear the interpreter console
clear()
plt.close('all')
# Prompts

FilepathofOriginal=raw_input("What is the PDF file to be extracted?")
drawing1=input('Whats the first drawing sheet you want to extract?')
drawing2=input('Whats the last drawing sheet you want to extract?')
# Engineer_of_record=raw_input("Who was the Engineer on Record?")
Engineer_of_record='SIEMANS'
Filepath=raw_input('Destination Filepath?')
    
# If Main category is Track, Signaling or Network Comm.(\Test Data or Agreement and Documents or Assembly)

#Setting Up Workspace folder to run Tiff OCR to grab title block information (Look to line 117)
Folderpath_Of_workspace=os.path.split(FilepathofOriginal)
FileTitle=Folderpath_Of_workspace[1].replace('.pdf','')
Filelist=os.listdir(Folderpath_Of_workspace[0])
Filelist=filter(lambda k: FileTitle in k, Filelist)
Filelist=filter(lambda k: 'Page' in k, Filelist)
Filelist=filter(lambda k: '.tif' in k, Filelist)# Only files from Filenames list
    
# From=raw_input("From Stationing (Don't forget the +)")
From=''
# To=raw_input("To Stationing (Don't forget the +)")
To=''
date=raw_input("What is the date of the drawing?")
os.chdir(Filepath) # Change directory
    
filenamepdf=file(FilepathofOriginal,'rb')
inputpdf=PdfFileReader(filenamepdf) # Run through PdfFileReader engine

# Record category into hyperlinks.csv, by knowing the filepath directory. 
Line_segment, Main_cat, Sub_cat, Generalname=ExtractFileCategories(Filepath)

# Defining temp hyperlink .txt file
hyperlink_directory='P:\Current_Configuration\MTS_Rails\Metadata Extras\hyperlinks.csv' 
# Extract pages from .PDF into respective destination folder and record transfer to hyperlink.csv file for later import into Metadata File
while drawing1 <= drawing2:
        
    #Open tiff as an array
    os.chdir(Folderpath_Of_workspace[0])
    nameOtiff=Filelist[drawing1-1]
    im=cv.LoadImageM(nameOtiff) # Use OpenCV to convert image to numpy.array
    imarray=numpy.asarray(im) # Turn image into array
    plt.figure()
    plt.imshow(imarray)
    plt.show()
        
    # Extract Title block information
    croppedTitle=imarray[2010:2150,2450:3050,:] # Index array to crop picture [Height , Width]
    im=imagegrab(croppedTitle)
    Title=image_to_string(im) # Using tesseract to read text on file
    Drawing_Title=Title.replace("\n"," ")
    print Drawing_Title
        
    #Extract Drawing No.
    croppedDrawing_Num=imarray[2100:2120,3120:3230] # Index array to crop picture [Height , Width]
    im=imagegrab(croppedDrawing_Num)
    Drawing_Num=image_to_string(im) # Using tesseract to read text on file
    Drawing_Num=Drawing_Num.replace("\n","")
    Drawing_Num=Drawing_Num.replace("()","0")
    Drawing_Num=Drawing_Num.replace("[]","0")
    Drawing_Num=Drawing_Num.replace(")(","X")
    Drawing_Num=Drawing_Num.replace(" ","")
    Drawing_Num_End=Drawing_Num[5:]
    Drawing_Num_End=Drawing_Num_End.replace("B","8")        
    Drawing_Num=FileTitle[:5]+Drawing_Num_End
    print Drawing_Num
        
    os.chdir(Filepath)
    # Extract PDF sheet(s)
    output=PdfFileWriter() # Create new empty PDF sheet
    output.addPage(inputpdf.getPage(drawing1-1)) 
    New_string=Drawing_Num+'.pdf' # Modify string name
    NewFilename=os.path.join(Filepath,New_string)
        
    #Write to csv file
    additional_line=['=HYPERLINK('+'"'+NewFilename+'"'+','+'"'+New_string+'")'+';'+date+';'+ 'MTS Rail'+';'+ Line_segment+';'+'Segment(Hidden)'+';'+Main_cat+';'+ \
        Sub_cat+';'+'As-Built'+';'+Generalname+';'+Drawing_Num+';'+Drawing_Title+';'+Engineer_of_record+';'+From+';'+To+'; ; ; ; ; ; ; ; ; ; ;']
    PrintToCSVReport(hyperlink_directory,additional_line) # Prints information to CSVfile
        
    outputFile=file(NewFilename,'wb') 
    drawing1=drawing1+1
    print drawing1
    with open(NewFilename,'wb'):
        output.write(outputFile)
    outputFile.close()
filenamepdf.close()
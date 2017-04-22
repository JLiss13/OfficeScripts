#Read DSD Invoices as Tiffs to extract their associated PDF files and
#organize them in their respective folders.
#ALWAYS SCAN THE INVOICES AS B/W @ DPI 600x600

from PIL import Image
from pytesser import *
import numpy
import os
import cv
import matplotlib.pyplot as plt
from pyPdf import PdfFileWriter, PdfFileReader
import time, datetime

def PrintToCSVReport(ReportFile,Data1):
    all_content=[]
    with open(ReportFile) as f:
        all_lines = [line.strip() for line in f]
    all_content+=all_lines #aka all_content = all_content+ all_lines
    # Write gathered information to the destination csv file
    all_content+=Data1
    with open(ReportFile, 'w') as f: # 'w'=Write permissions to file
        for line in all_content:
            print >> f, line # Inserts line of appended array to each new line of "DSD Invoice Organization Report.txt"

plt.close('all')
cwd = os.getcwd()
FilepathofOriginal=cwd +'Original Scanned PDF Files\DSD_Invoices_Historical.pdf'
filenamePDf=file(FilepathofOriginal,'rb') # Read PDF
inputpdf=PdfFileReader(filenamePDf) # Run through PdfFileReader engine
Folderpathdestination=cwd + 'Account Statements' # Place Tiff files in this same folder to be read
Folderpath_Of_code=cwd;
os.chdir(Folderpath_Of_code)
# nameOtiff=raw_input('name of imagefile to be modified?')
Filelist=os.listdir(Folderpath_Of_code)
Filelist=filter(lambda k: 'DSD' in k, Filelist)
Filelist=filter(lambda k: '.tif' in k, Filelist)# only files from Filenames list
DSDInvoiceReport=cwd + 'Report.txt'
drawing_num=raw_input('What is the beginning drawing number?')
drawing_num=int(drawing_num)
PDFFileName=''

#Loop over all DSD tiff files
for nameOtiff in Filelist:
    #plt.close('all')
    Folderpath_Of_code=cwd
    os.chdir(Folderpath_Of_code)
    nameOtiff=Filelist[drawing_num]
    print nameOtiff
    im=cv.LoadImageM(nameOtiff) # Use OpenCV to convert image to numpy.array
    imarray=numpy.asarray(im) # Turn image into array
    plt.figure()
    plt.imshow(imarray)
    plt.show()

    # Extract the Project Number
    croppedProject_Num=imarray[1380:1445,400:600:] # Index array to crop picture [Height , Width]
    croppedProject_Num_im=Image.fromarray(croppedProject_Num)
    croppedProject_Num_im.save('Project_Num.tif') # created new cropped tiff file
    im=Image.open('Project_Num.tif')
    Project_Num_text=image_to_string(im) # Using tesseract to read text on file
    Project_Num_text=Project_Num_text.replace('\n','') # String Cleaning
    Project_Num_text=Project_Num_text.replace(' ','')
    Project_Num_text=Project_Num_text.replace(':','')
    Project_Num_text=Project_Num_text.replace('O','0')
    Project_Num_text=Project_Num_text.replace('o','')
    Project_Num_text=Project_Num_text.replace('~','')
    Project_Num_text=Project_Num_text[0:6]

    plt.figure()
    plt.imshow(croppedProject_Num)
    plt.show()
    print Project_Num_text
    #Project_Num_text='329726'

    #Extract the Invoice Dates
    croppedProject_Date=imarray[180:240,1625:1850,:] # Index array to crop picture [Height , Width]
    croppedProject_Date_im=Image.fromarray(croppedProject_Date)
    croppedProject_Date_im.save('Project_Date.tif') # created new cropped tiff file
    im=Image.open('Project_Date.tif')
    Project_Num_Date=image_to_string(im) # Using tesseract to read text on file
    Project_Num_Date=Project_Num_Date.replace('I','/') # String Cleaning
    Project_Num_Date=Project_Num_Date.replace('l','/')
    Project_Num_Date=Project_Num_Date.replace('!','/')
    Project_Num_Date=Project_Num_Date.replace("'",'1')
    Project_Num_Date=Project_Num_Date.replace('\n','')
    Project_Num_Date=Project_Num_Date.replace('S','8')
    Project_Num_Date=Project_Num_Date.replace('B','8')
    Project_Num_Date=Project_Num_Date.replace('{','')
    Project_Num_Date=Project_Num_Date.replace('}','')
    Project_Num_Date=Project_Num_Date.replace('[','')
    Project_Num_Date=Project_Num_Date.replace(']','')
    Project_Num_Date=Project_Num_Date.replace('(','')
    Project_Num_Date=Project_Num_Date.replace(')','')
    Project_Num_Date=Project_Num_Date.replace(' ','')
    Project_Num_Date=Project_Num_Date.replace('//','/')
    Project_Num_Date=Project_Num_Date.replace('Q','0')
    Project_Num_Date=Project_Num_Date.replace('O','0')
    Project_Num_Date=Project_Num_Date.replace('U','0')
    Project_Num_Date=Project_Num_Date.replace('n','')
    Project_Num_Date=Project_Num_Date.replace('o','')
    Project_Num_Date=Project_Num_Date.replace('~','')
    Project_Num_Date=Project_Num_Date.replace('Z','2')
    Project_Num_Date=Project_Num_Date.replace('A','')
    
    plt.figure()
    plt.imshow(croppedProject_Date)
    plt.show()
    print Project_Num_Date
    Project_Num_Date='1/31/2015'
     
    # Determine if Project_Number and Project Dates are correct
    Num_validater=str(Project_Num_text.isdigit())
    if Num_validater=='False':# Check to see if Project_Num_text is a num 
        break
        break
    Project_Num_Date=Project_Num_Date.split('/')
    Project_Num_Date=[int(i) for i in Project_Num_Date]
    Date_validater=numpy.sum(Project_Num_Date)
    Project_Num_Date=[str(i) for i in Project_Num_Date]
    Project_Num_Date='/'.join(Project_Num_Date)
    print Project_Num_Date
    
    #Place sheets into their respective folders
    Project_Num_text=str(Project_Num_text)
    for root, dirs, files in os.walk(Folderpathdestination,topdown=False):
        if any(Project_Num_text in directory for directory in dirs):
            for directory in dirs:
                if Project_Num_text in directory:
                    print directory
                    os.chdir(os.path.join(root, directory))
                    files=os.listdir(os.path.join(root, directory))
                    files=filter(lambda k: Project_Num_text in k, files) 
                    files.sort(key=os.path.getmtime) # Sort to grab only the most recent file
                    New_string=files[-1]
                    print New_string
                    PDFFileName=New_string.split('_')
                    print PDFFileName
                    Project_Num_Date=Project_Num_Date.split('/')
                    print Project_Num_Date
                    PDFFileName[len(PDFFileName)-3]=Project_Num_Date[0]
                    PDFFileName[len(PDFFileName)-2]=Project_Num_Date[1]
                    PDFFileName[len(PDFFileName)-1]=Project_Num_Date[2]+'.pdf'
                    PDFFileName='_'.join(PDFFileName)
                    Project_Num_Date='/'.join(Project_Num_Date)
                    print PDFFileName
                    Filepath=os.path.join(root,directory)
                    NewFileDir=os.path.join(Filepath,PDFFileName)
                    output=PdfFileWriter() # Create new empty PDF sheet
                    output.addPage(inputpdf.getPage(drawing_num))
                    output.addPage(inputpdf.getPage(drawing_num+1))
                    outputFile=file(NewFileDir,'wb')
                    with open(NewFileDir,'wb'):
                        output.write(outputFile)
                    outputFile.close()
                    date_time=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                    additional_line=[str(drawing_num)+';'+PDFFileName+';'+Project_Num_text+';'+Project_Num_Date+';'+date_time]
                    PrintToCSVReport(DSDInvoiceReport,additional_line)
            '''
            else:
                date_time=datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                additional_line=[str(drawing_num)+';'+'CHECK TIFF FILE'+';'+Project_Num_text+';'+Project_Num_Date+';'+date_time]
                PrintToCSVReport(DSDInvoiceReport,additional_line) 
                '''
    drawing_num=drawing_num+2
filenamePDf.close()
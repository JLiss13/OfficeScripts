#Created by Jordan Liss
#Extract pages from .PDF into current directory
import os
from pyPdf import PdfFileWriter, PdfFileReader
FilepathofOriginal=raw_input('What document do you want to extract?')
drawing1=input('Whats the first drawing sheet you want to extract?')
drawing2=input('Whats the last drawing sheet you want to extract?')
filenamePDf=file(FilepathofOriginal,'rb') # Read PDF
inputpdf=PdfFileReader(filenamePDf) # Run through PdfFileReader engine
Filepath=raw_input('Where do you want the individual files stored')
os.chdir(Filepath) # Change directory
Generalname=FilepathofOriginal[len(FilepathofOriginal)-19:len(FilepathofOriginal)-4] # Extract Title of File
notation=raw_input("What letter(s) does the new drawing number begin with?") # Must input a string with apostrophes
print notation
firstdnumber=input("What is the new beginning drawing number?")  # Set first drawing number
print firstdnumber
while drawing1 <= drawing2: 
    output=PdfFileWriter() # Create new empty PDF sheet
    output.addPage(inputpdf.getPage(drawing1-1)) 
    New_string=Generalname+'_'+notation+str(firstdnumber) # Modify string name
    NewFilename=FilepathofOriginal.replace(Generalname,New_string)
    outputFile=file(NewFilename,'wb') 
    firstdnumber=firstdnumber+1
    drawing1=drawing1+1
    with open(NewFilename,'wb'):
        output.write(outputFile)
    outputFile.close()
filenamePDf.close()
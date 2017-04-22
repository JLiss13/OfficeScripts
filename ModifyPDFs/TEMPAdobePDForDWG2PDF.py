import os
from PyPDF2 import PdfFileReader
hyperlink=raw_input("What is the folder directory?")
os.chdir(hyperlink) # Change directory
files=os.listdir(hyperlink) # display list in directory
FilesPDF=filter(lambda k: '.pdf' in k, files) # Make list of only pdf files
Filenumber=0
# while Filenumber < len(FilesPDF):
filename=os.path.join(hyperlink,FilesPDF[Filenumber])
fin=file(filename,'rb') # Open File
pdf_in=PdfFileReader(fin) # use PyPDF2 file reader
info=pdf_in.getDocumentInfo()
info=dict(info) # convert to python dictionary
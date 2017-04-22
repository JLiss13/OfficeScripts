#Writing Metadata into PDF from Attext file
from PyPDF2 import PdfFileWriter, PdfFileReader
# filename=raw_input("Pdf file hyperlink?")
filename="M:\Engineering\ESo\Standard Plan\Updated\OCS\Typical Pushoff Cantilever Assemblies Layout1 (1).pdf"
fin=file(filename,'rb') # Open File
pdf_in=PdfFileReader(fin) # use PyPDF2 file reader

# Grabbing and processing information from Attext produced .txt
# AttFile=raw_input("File with attributes?")
AttFile="C:\Users\jli\Documents\CurrentConfiguration\Typical Pushoff Cantilever Assemblies.txt"
AttFiletemp=open(AttFile,'r')
Attributes=[]
for row in AttFiletemp:
    Attributes.append(row.strip().split(','))
# print Attributes

AttributesTitle=Attributes[0][0]+';'+Attributes[0][1]+';'+Attributes[0][3]
AttributesTitle=AttributesTitle.replace("'",'')

from PyPDF2.generic import NameObject, createStringObject
writer=PdfFileWriter() # New new pdf file
for page in range(pdf_in.getNumPages()):
    writer.addPage(pdf_in.getPage(page))
infoDict=writer._info.getObject() # Grab existing pdf info
info=pdf_in.documentInfo
for key in info:
    infoDict.update({NameObject('/Title'): createStringObject(AttributesTitle)})
info.update({NameObject('/Title'): createStringObject(AttributesTitle)})
print infoDict

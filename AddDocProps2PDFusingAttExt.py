#Writing Metadata into PDF from Attext file through the whole folder
import os
from CurCon_Module import MetadataInfoWrite
from PyPDF2 import PdfFileWriter, PdfFileReader
hyperlink=raw_input("What is the folder directory?")
os.chdir(hyperlink) # Change directory
files=os.listdir(hyperlink) # display list in directory
FilesPDF=filter(lambda k: '.pdf' in k, files) # Make list of only pdf files
FilesAtt=filter(lambda k:'.txt' in k, files) # Make list of only txt files
Filenumber=0
while Filenumber < len(FilesAtt):
    # Grab Attribute Extraction txt
    AttFile=FilesAtt[Filenumber]
    AttFiletemp=AttFile.replace('.txt','')
    #Match Attribute Extraction txt with associated PDF file
    MatchingPDF=filter(lambda x: AttFiletemp in x, FilesPDF)
    # Open Attribute Extraction txt
    AttFilePath=os.path.join(hyperlink,AttFile)
    AttFilePathtemp=open(AttFilePath,'r')
    Attributes=[]
    for row in AttFilePathtemp:
        Attributes.append(row.strip().split(','))
    # Open PDF file. Because we can't rewrite Metadata per se.
    # We have to make a copy and rename the modified copy to overwrite original file
    filename=os.path.join(hyperlink,MatchingPDF[0])
    fin=file(filename,'rb') # Open File
    pdf_in=PdfFileReader(fin) # use PyPDF2 file reader
    info=pdf_in.getDocumentInfo() # Grab document info from original pdf
    info=dict(info) # convert to python dictionary
    writer=PdfFileWriter() # Write new pdf file
    for page in range(pdf_in.getNumPages()): # Get all the pages in the pdf
        writer.addPage(pdf_in.getPage(page))

    MetadataTitles=['/Subject','/Title','/Keywords'] # Metadata titles found in PDF
    # Run through list of Metadata tags to replace all with block attributes    
    # Subject
    AttributesTitle=Attributes[0][0]
    AttributesTitle=AttributesTitle.replace("'",'') # Eliminate extra quotes
    info[MetadataTitles[0]]=AttributesTitle # Add new Metadata
    # Title
    AttributesTitle=Attributes[0][1]+' '+Attributes[0][2]+' '+Attributes[0][3]
    AttributesTitle=AttributesTitle.replace("'",'') # Eliminate extra quotes
    info[MetadataTitles[1]]=AttributesTitle # Add new Metadata
    # Additional Info.
    AttributesTitle=Attributes[0][4]+';'+Attributes[0][5]
    AttributesTitle=AttributesTitle.replace("'",'') # Eliminate extra quotes
    info[MetadataTitles[2]]=AttributesTitle  # Add new Metadata
    
    # Write new metadata dictionary into pdf 
    MetadataInfoWrite(filename, fin, info, writer) 
    Filenumber=Filenumber+1
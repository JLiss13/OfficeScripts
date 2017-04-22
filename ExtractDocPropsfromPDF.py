#Writing Metadata into PDF from Attext file through the whole folder
import os
from CurCon_Module import PrintToCSVReport
from PyPDF2 import PdfFileReader
#Prompts
Files_Directory=raw_input("What is the folder directory?")
hyperlink_directory='P:\Current_Configuration\MTS_Rails\Metadata Extras\hyperlinks.csv'
os.chdir(Files_Directory)
files=os.listdir(Files_Directory) # display list in directory
FilesPDF=filter(lambda k: '.pdf' in k, files) # Make list of only pdf files
for filename in FilesPDF:
    print filename
    fin=file(filename,'rb') # Open File
    pdf_in=PdfFileReader(fin) # use PyPDF2 file reader
    info=pdf_in.getDocumentInfo() # Grab document info from original pdf
    info=dict(info) # convert to python dictionary
    MetadataTitles=['/Subject','/Author','/Title','/Keywords'] # Metadata titles found in PDF
    NewFilename=os.path.join(Files_Directory,filename)
    New_string=filename
    Keyword_Info=info[MetadataTitles[3]]
    Keyword_Info=Keyword_Info.split(';')
    Date=Keyword_Info[0]
    Line_segment=Keyword_Info[2]
    Main_cat=info[MetadataTitles[0]]
    Sub_cat=Keyword_Info[4]
    Generalname=Keyword_Info[6]
    Drawing_Num=Keyword_Info[7]
    Drawing_title=info[MetadataTitles[2]]
    Engineer_of_record=Keyword_Info[8]
    From=Keyword_Info[9]
    To=Keyword_Info[10]
    additional_line=['=HYPERLINK('+'"'+NewFilename+'"'+','+'"'+New_string+'")'+';'+Date+';'+ 'MTS Rail'+';'+ Line_segment+';'+'Segment(Hidden)'+';'+Main_cat+';'+ \
        Sub_cat+';'+'As-Built'+';'+Generalname+';'+Drawing_Num+';'+Drawing_title+';'+Engineer_of_record+';'+From+';'+To+'; ; ; ; ; ; ; ; ; ; ;']
    PrintToCSVReport(hyperlink_directory,additional_line) # Prints information to CSVfile
#Writing Metadata into PDF from Attext file through the whole folder
import os
import operator
from CurCon_Module import MetadataPDF, FindMissingFiles
from PyPDF2 import PdfFileWriter, PdfFileReader
#Prompts
Files_Directory=raw_input("What is the folder directory?")
CurCon_Data=raw_input("What is the file with CurCon metadata tags?")
os.chdir(Files_Directory) # Change directory
all_content_CSV, filesAlreadyFiled, filesNotFiled=FindMissingFiles(Files_Directory,CurCon_Data) # Check CurCon_Module
all_content_CSV=list(all_content_CSV) # convert into a list
all_content_CSV=reduce(operator.add,all_content_CSV)
files=os.listdir(Files_Directory) # display list in directory
FilesPDF=filter(lambda k: '.pdf' in k, files) # Make list of only pdf files
Filenumber=0
file_num=0
for filename in FilesPDF:
    print filename
    # Open PDF file. Because we can't rewrite Metadata per se.
    # We have to make a copy and rename the modified copy to overwrite original file
    fileurl=os.path.join(Files_Directory,filename)
    filenum=all_content_CSV.index(filename)
    subject=all_content_CSV[filenum+5]
    author=all_content_CSV[filenum+11]
    title=all_content_CSV[filenum+10]
    additional_info=all_content_CSV[filenum+1]+';'+all_content_CSV[filenum+2]+';'+ \
        all_content_CSV[filenum+3]+';'+all_content_CSV[filenum+4]+';'+all_content_CSV[filenum+5] +';'+ \
            all_content_CSV[filenum+6]+';'+all_content_CSV[filenum+7]+';'+all_content_CSV[filenum+8] +';'+ \
                all_content_CSV[filenum+9]+';'+all_content_CSV[filenum+11]+';'+ all_content_CSV[filenum+12] +';'+ \
                    all_content_CSV[filenum+13]
    # Place here lines to determine what the subject, title and additional_info is going to be.
    MetadataPDF(fileurl,subject,author,title,additional_info)
    Filenumber=Filenumber+1
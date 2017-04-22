#Write Only CurCon Data to CSV file from files that have not been organized already
from CurCon_Module import PrintToCSVReport
import os
import operator
import shutil

clear=lambda: os.system('cls') # clear the interpreter console
clear()

#Functions
def FindMissingFiles(Filepath,csvfile):
    Files=os.listdir(Filepath)
    #CSVtoCompare=raw_input("What's the CSV file to compare with?")
    all_content_CSV=[]
    with open(csvfile) as data_file:
        for line in data_file:
            all_content_CSV.append(line.strip().split(','))
    filesAlreadyFiled=[]
    filesNotFiled=[]
    for filename in Files:
        if any(filename in lines for lines in all_content_CSV):
            filesAlreadyFiled.append(filename)
        else:
            filesNotFiled.append(filename)
    all_content_CSV=list(all_content_CSV) # convert into a list
    all_content_CSV=reduce(operator.add,all_content_CSV)
    return (all_content_CSV, filesAlreadyFiled,filesNotFiled)

#User Input Prompts
FilePath=raw_input('Path of directory being checked?')
#filetype=raw_input('What is the filetype extension being checked?')
filetype='.dwg'
#CSVFile=raw_input('Path of CSV file with list of files already in CurCon?')
CSVFile='P:\Current_Configuration\MTS_Rails\Metadata Extras\BlueSignalingCurConInventory.csv'
#hyperlinkfile=raw_input('Path of CSV file you want to print hyperlinks to?')
hyperlinkfile='P:\Current_Configuration\MTS_Rails\Metadata Extras\hyperlinksfromdirectory.csv'
#Contract_Name=raw_input('What is the name of the project contract?')
Contract_Name='CIP 1210020'
FirstFile=input('What number file should be first?')
#Programming
all_files,filesAlreadyinCurcon,filesNotinCurcon=FindMissingFiles(FilePath,CSVFile)
filesNotinCurcon=filter(lambda k:k.endswith(filetype), filesNotinCurcon)

#print "Files not filed" + filesNotinCurcon
print filesNotinCurcon

filenum=FirstFile-1
while filenum <len(filesNotinCurcon):
    Individual_File=filesNotinCurcon[filenum]
    print str(filenum+1)+" "+"File being processed is" +" "+Individual_File
    Drawing_number=Individual_File.replace(filetype,'')
    fileindex=all_files.index(Drawing_number)
    Date=all_files[fileindex-8]
    Generalname=all_files[fileindex-7]
    Line_segment=all_files[fileindex-6]
    Main_cat=all_files[fileindex-4] 
    Sub_cat=all_files[fileindex-3]
    Drawing_Title=all_files[fileindex+1]
    Engineer=all_files[fileindex+2]
    To=all_files[fileindex+3]
    From=all_files[fileindex+4]
    Old_Filepath=os.path.join(FilePath,filesNotinCurcon[filenum]) # Old filepath
    Individual_Filepaths=os.path.join("P:\Current_Configuration","MTS_Rails", Line_segment, Main_cat, Sub_cat, filesNotinCurcon[filenum])
    shutil.copy2(Old_Filepath,Individual_Filepaths) #Copy file to a new destination
    additional_line=['=HYPERLINK('+'"'+ Individual_Filepaths +'"'+','+'"'+Individual_File+'")'+';'+Date+';'+ Generalname+';'+ Line_segment +';'+'Segment(Hidden)'+';'+Main_cat+';'+ \
        Sub_cat+';'+'As-Built'+';'+Contract_Name+';'+Drawing_number+';'+Drawing_Title+';'+Engineer+';'+ To +';'+ From +'; ; ; ; ; ; ; ; ; ; ; ;']
    PrintToCSVReport(hyperlinkfile,additional_line)
    filenum=filenum+1

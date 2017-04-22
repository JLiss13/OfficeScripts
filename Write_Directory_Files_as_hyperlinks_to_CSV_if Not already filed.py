#Write Only CurCon Data to CSV file from files that have not been organized already
import os
from CurCon_Module import ExtractFileCategories, FindMissingFiles, PrintToCSVReport

clear=lambda: os.system('cls') # clear the interpreter console
clear()

#User Input Prompts
Filepath=raw_input('Path of directory being checked?')
#filetype=raw_input('What is the filetype extension being checked?')
filetype='.pdf'
#CSVFile=raw_input('Path of CSV file with list of files already in CurCon?')
CSVFile='P:\Current_Configuration\MTS_Rails\Metadata Extras\hyperlinkswithtitleBlueSignaling.csv'
#hyperlinkfile=raw_input('Path of CSV file you want to print hyperlinks to?')
hyperlinkfile='P:\Current_Configuration\MTS_Rails\Metadata Extras\hyperlinksfromdirectory.csv'
#Contract_Name=raw_input('What is the name of the project contract?')
Contract_Name='CIP 1210020'

#Programming
all_files,filesAlreadyinCurcon,filesNotinCurcon=FindMissingFiles(Filepath,CSVFile)
filesNotinCurcon=filter(lambda k:k.endswith(filetype), filesNotinCurcon)
Generalname, Line_segment, Main_cat, Sub_cat=ExtractFileCategories(Filepath)

filenum=0
while filenum <len(filesNotinCurcon):
    Individual_Filepaths=os.path.join(Filepath,filesNotinCurcon[filenum])
    Individual_File=filesNotinCurcon[filenum]
    Drawing_number=Individual_File.replace(filetype,'')
    additional_line=['=HYPERLINK('+'"'+ Individual_Filepaths +'"'+','+'"'+Individual_File+'")'+';'+'12/11'+';'+ 'MTS Rail'+';'+ Line_segment +';'+'Segment(Hidden)'+';'+Main_cat+';'+ \
        Sub_cat+';'+'As-Built'+';'+Contract_Name+';'+Drawing_number+';'+'Drawing Title'+';'+'SIEMENS'+'; ; ; ; ; ; ; ; ; ; ; ; ; ;']
    PrintToCSVReport(hyperlinkfile,additional_line)
    filenum=filenum+1
#For write hyperlinks in a directory to a .csv or .txt
import os 
import numpy
import datetime
Folderpath=raw_input('Destination Folderpath?')
#Name=raw_input('Common name found in title? (Plus any underscores or blanks after)')
# FilestobeChanged=input("What is the last file number that needs to be changed?")
Name="LRT 1142100.1_San Altos_"
hyperlink_directory='M:\Engineering\Current_Configuration\MTS_Rails\hyperlinks.csv'
Files=os.listdir(Folderpath)
filenum=0
# Obtain Date Modified Time Stamp
Date_Modified=numpy.zeros(len(Files))
while filenum <len(Files):
    Folderpath2=os.path.join(Folderpath,Files[filenum])
    Date_Modified[filenum]=os.path.getmtime(Folderpath2)
    filenum=filenum+1
#Sort the Files Array into a new array called NewFiles grabbing only
#date modified times from october 13th 2014 and on.
Date_Modified_Index=[i for i,v in enumerate(Date_Modified>1.413e9)if v]
NewFiles=['']*len(Date_Modified_Index)
filenum=0
while filenum < len(Date_Modified_Index):
    NewFiles[filenum]=Files[Date_Modified_Index[filenum]]
    TimeStamp=datetime.datetime.fromtimestamp(Date_Modified[Date_Modified_Index[filenum]]).strftime("%y-%m-%d %H:%M:%S")
    print NewFiles, TimeStamp
    filenum=filenum+1
# Files=filter(lambda k: '.dwg' in k, Files) # Filters out only strings that have .dwg
# If Main category is Track, Signaling or Network Comm.(\Test Data or Agreement and Documents or Assembly)
Words_1=["Track","Signaling","Assembly","TestData","AgreementandDocuments"]
Words_3=["Traction Power","Fiber Cable Plan","Fiber Cabling Schedule","Fiber Splicing Diagram","Single Block Diagram"]
for item in Words_1:  
    if item in Folderpath:
        Pathsplit=os.path.split(Folderpath)
        Path_Sub_cat1=os.path.split(Pathsplit[0])
        Sub_cat=Path_Sub_cat1[1]
        Path_Main_cat1=os.path.split(Path_Sub_cat1[0])
        Main_cat=Path_Main_cat1[1]
        Path_Line_segment=os.path.split(Path_Main_cat1[0])
        Line_segment=Path_Line_segment[1]
# If Main category is Stations
if "Stations" in Folderpath:
    Pathsplit=os.path.split(Folderpath)
    Path_Sub_cat2=os.path.split(Pathsplit[0])
    Sub_cat=Path_Sub_cat2[1]
    Path_Main_cat2=os.path.split(Path_Sub_cat2[0])
    Main_cat=Path_Main_cat2[1]
    Path_Station2=os.path.split(Path_Main_cat2[0])
    Path_Line_segment2=os.path.split(Path_Station2[0])
    Line_segment=Path_Line_segment2[1]
# If Main category is Traction Power or Network Comm.\Network Diagram
for item in Words_3:
    if item in Folderpath:
        Pathsplit3=os.path.split(Folderpath)
        Path_Sub_Sub_cat3=os.path.split(Pathsplit3[0])
        Sub_Sub_cat=Path_Sub_Sub_cat3[1]
        Path_Sub_cat3=os.path.split(Path_Sub_Sub_cat3[0])
        Sub_cat=Path_Sub_cat3[1]
        Sub_cat=Sub_cat+'-'+Sub_Sub_cat
        Path_Main_cat3=os.path.split(Path_Sub_cat3[0])
        Main_cat=Path_Main_cat3[1]
        Path_Line_segment=os.path.split(Path_Main_cat3[0])
        Line_segment=Path_Line_segment[1]
filenum=0
while filenum < len(NewFiles):
    all_content=[]
    with open(hyperlink_directory) as f:
        all_lines = [line.strip() for line in f]
        all_content+=all_lines #aka all_content = all_content+ all_lines
    # Write gathered information to the destination csv file
    Individual_Folderpaths=os.path.join(Folderpath,NewFiles[filenum])
    Individual_File=NewFiles[filenum]
    Drawing_number=Individual_File[len(Name):Individual_File.find(".dwg" or "pdf")] # Grab the drawing number
    additional_line=['=HYPERLINK('+'"'+ Individual_Folderpaths +'"'+','+'"'+Individual_File+'")'+';'+'3/14'+';'+ 'MTS Rail'+';'+ Line_segment +';'+'Segment(Hidden)'+';'+Main_cat+';'+ \
        Sub_cat+';'+'As-Built'+';'+Name+';'+Drawing_number+';'+'Drawing Title'+';'+'MTDB']
    all_content+=additional_line
    filenum=filenum+1
    with open(hyperlink_directory, 'w') as f: # 'w'=Write permissions to file
        for line in all_content:
            print >> f, line # Inserts line of appended array to each new line of hyperlink.csv file
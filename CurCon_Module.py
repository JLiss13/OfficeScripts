#CurCon Module with many useful functions for file organizing, CSV printing, Image grabbing and file finder
import os
from PIL import Image
import matplotlib.pyplot as plt
import pickle

def ExtractFileCategories(Filepath):
    # If Main category is Track, Signaling or Network Comm.(\Test Data or Agreement and Documents or Assembly)
    Words_1=["Track","Signaling","Assembly","TestData","AgreementandDocuments"]
    Words_3=["Traction Power","Fiber Cable Plan","Fiber Cabling Schedule","Fiber Splicing Diagram","Single Block Diagram"]
    for item in Words_1:  
        if item in Filepath:
            Pathsplit=os.path.split(Filepath)
            Path_Sub_cat1=os.path.split(Pathsplit[0])
            Sub_cat=Path_Sub_cat1[1]
            Path_Main_cat1=os.path.split(Path_Sub_cat1[0])
            Main_cat=Path_Main_cat1[1]
            Path_Line_segment=os.path.split(Path_Main_cat1[0])
            Line_segment=Path_Line_segment[1]
    # If Main category is Stations
    if "Stations" in Filepath:
        Pathsplit=os.path.split(Filepath)
        Path_Sub_cat2=os.path.split(Pathsplit[0])
        Sub_cat=Path_Sub_cat2[1]
        Path_Main_cat2=os.path.split(Path_Sub_cat2[0])
        Main_cat=Path_Main_cat2[1]
        Path_Station2=os.path.split(Path_Main_cat2[0])
        Path_Line_segment2=os.path.split(Path_Station2[0])
        Line_segment=Path_Line_segment2[1]
    # If Main category is Traction Power or Network Comm.\Network Diagram
    for item in Words_3:
        if item in Filepath:
            Pathsplit3=os.path.split(Filepath)
            Path_Sub_Sub_cat3=os.path.split(Pathsplit3[0])
            Sub_Sub_cat=Path_Sub_Sub_cat3[1]
            Path_Sub_cat3=os.path.split(Path_Sub_Sub_cat3[0])
            Sub_cat=Path_Sub_cat3[1]
            Sub_cat=Sub_cat+'-'+Sub_Sub_cat
            Path_Main_cat3=os.path.split(Path_Sub_cat3[0])
            Main_cat=Path_Main_cat3[1]
            Path_Line_segment=os.path.split(Path_Main_cat3[0])
            Line_segment=Path_Line_segment[1]
    Generalname=os.path.split(Filepath)
    Generalname=Generalname[1]# Extract Title of File
    return (Line_segment, Main_cat, Sub_cat, Generalname) 
    
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
    return (filesAlreadyFiled, filesNotFiled)
            
def imagegrab(crop):
    cropped_im=Image.fromarray(crop)
    cropped_im.save('croppedimage.tif') # created new cropped tiff file
    im=Image.open('croppedimage.tif')
    plt.figure()
    plt.imshow(im)
    plt.show()
    return im
       
def PrintToCSVReport(ReportFile,Data1):
    all_content=[]
    with open(ReportFile) as f:
        all_lines = [line.strip() for line in f]
    all_content+=all_lines #aka all_content = all_content+ all_lines
    # Write gathered information to the destination csv file
    all_content+=Data1
    with open(ReportFile, 'w') as f: # 'w'=Write permissions to file
        for line in all_content:
            print >> f, line # Inserts line of appended array to each new line of
            
def savetext(inputvalue,savedvalue,index,): #save previous text for the next round of metadata input
    if inputvalue=='s': #Type s into any prompt and the previous input from the previous loop will be the current value
        savedvalue=pickle.load(open("save.p","rb")) # Dump pickle cache into saved variable
        inputvalue=savedvalue[index] #Save previous text to current text
    else:
        savedvalue[index]=inputvalue # Save new text to replace old text
        pickle.dump(savedvalue,open("save.p","wb"))  # save text to forever changing file
        return inputvalue        
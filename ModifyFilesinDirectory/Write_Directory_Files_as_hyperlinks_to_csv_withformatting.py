#For write hyperlinks in a directory to a .csv or .txt
import os 
import numpy as np
Filepath=input('Destination Filepath?') 
hyperlink_directory='M:\Engineering\Current_Configuration\MTS_Rails\hyperlinks.csv' 
Files=os.listdir(Filepath)
Filesdwg=filter(lambda k: '.dwg' in k, Files) # Filters out only strings that have .dwg in it
Filespdf=filter(lambda k: '.pdf' in k, Files) # Filters out only strings that have .pdf in it
filenum=0 # the set the beginning index of the file
n=0
all_content=np.matrix.transpose(np.array(xrange(0,len(Files))))
while filenum < len(Filespdf):
    # Write gathered information to the destination csv file
    Individual_Filedwgpaths=os.path.join(Filepath,Filesdwg[filenum])
    Individual_Filepdfpaths=os.path.join(Filepath,Filespdf[filenum])
    additional_line_pdf=['=HYPERLINK('+'"'+Individual_Filepdfpaths+'"'+','+'"'+Files[filenum]+'"'+');']
    additional_line_dwg=['=HYPERLINK('+'"'+Individual_Filedwgpaths+'"'+','+'"'+Files[filenum]+'"'+');']
    all_content[n]=additional_line_pdf
    all_content[n+1]=additional_line_dwg
    filenum=filenum+1
    n=n+2
    with open(hyperlink_directory, 'w') as f: # 'w'=Write permissions to file
        for line in all_content:
            print >> f, line # Inserts line of appended array to each new line of hyperlink.csv file

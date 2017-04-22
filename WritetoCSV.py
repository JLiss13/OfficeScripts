# Create .csv file in the current configuration folder that has hyperlinks with file characteristics (hyperlink name,main category, sub category, drawing No.)
# Written by Jordan Liss
import os
# Read csv file using numpy
Curr_Con_directory='M:\Engineering\Current_Configuration\MTS_Rails' 
hyperlinksfile='hyperlinks.csv'
hyperlinksfile_path=os.path.join(Curr_Con_directory,hyperlinksfile) # Make hyperlink sheet path
all_content=[]
with open(hyperlinksfile_path) as f:
    all_lines = [line.strip() for line in f]
    all_content+=all_lines #aka all_content = all_content+ all_lines
# Write appended information to the destination csv file
# Insert lines 
extra_lines=[NewFilename+';'+ 'File Date'+';'+ 'Transit Type']
all_content+=extra_lines
with open(hyperlinksfile_path, 'w') as f: # 'w'=Write permissions to file
    for line in all_content:
        print >> f, line 
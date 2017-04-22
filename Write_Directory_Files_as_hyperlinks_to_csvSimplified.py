#For write hyperlinks in a directory to a .csv or .txt
import os 
Filepath=input('Destination Filepath?')
hyperlink_directory='M:\Engineering\Current_Configuration\MTS_Rails\hyperlinksfromdirectory.csv'
Files=os.listdir(Filepath)
filenum=0
while filenum < len(Files)-1:
    all_content=[]
    with open(hyperlink_directory) as f:
        all_lines = [line.strip() for line in f]
        all_content+=all_lines #aka all_content = all_content+ all_lines
    # Write gathered information to the destination csv file
    Individual_Filepaths=os.path.join(Filepath,Files[filenum])
    Individual_File=Files[filenum]
    additional_line=['=HYPERLINK('+'"'+ Individual_Filepaths+'"'+','+'"'+Individual_File+'")'+';']
    all_content+=additional_line
    filenum=filenum+1
    with open(hyperlink_directory, 'w') as f: # 'w'=Write permissions to file
        for line in all_content:
            print >> f, line # Inserts line of appended array to each new line of hyperlink.csv file
    

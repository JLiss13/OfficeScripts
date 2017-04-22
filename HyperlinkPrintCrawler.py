import os 
directory=input('Parent Directory?')
hyperlink_directory='M:\Engineering\Current_Configuration\MTS_Rails\hyperlinksfromdirectory.csv'
filenum=0
for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".pdf"):
            all_content=[]
            with open(hyperlink_directory) as f:
                all_lines = [line.strip() for line in f]
                all_content+=all_lines #aka all_content = all_content+ all_lines
            # Write gathered information to the destination csv file
            Individual_Filepaths=os.path.join(root,file)
            Individual_File=file
            additional_line=['=HYPERLINK('+'"'+ Individual_Filepaths+'"'+','+'"'+Individual_File+'")'+';']
            all_content+=additional_line
            with open(hyperlink_directory, 'w') as f: # 'w'=Write permissions to file
                for line in all_content:
                    print >> f, line # Inserts line of appended array to each new line of hyperlink.csv file
    
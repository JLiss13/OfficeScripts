#Created by Jordan Liss
# Replace any string in a file name
import os
Folder='C:\Users\jli\Dropbox\SANDAG'
Filenames=os.listdir(Folder)
for file_name in Filenames:
        string=file_name[len(file_name)-7:len(file_name)-4] # Find the section of the filename string to replace
        old_file_path=os.path.join(Folder,file_name) # Grab old file path
        file_name=file_name.replace(string,"yoyo") # Replace the section of the filename string to replace with "yoyo"
        new_file_path=os.path.join(Folder,file_name) # Create new file with modified filename
        print new_file_path # print progress of for loop
        os.rename(old_file_path,new_file_path) #rename the old file path with the new file path
#Created by Jordan Liss
# Replace any string in a file name
import os
# Part1Folder='M:\Engineering\Current_Configuration\MTS_Rails\Downtown (Bayside, C St, Park, Broadway)' # Grab large filepath
# Part2Folder='Track\Civil\LRT 450_Bayside' # Grab part 2 of large filepath
Folder=raw_input("What directory are you working in?") # Must input a string with apostrophes
print Folder
Old_string=raw_input("What strings of filename do you want to replace?")
print Old_string
New_string=raw_input("What do you want the old string to be replaced with?")
print New_string
Filenames=os.listdir(Folder) # Make list of directory a string array
for file_name in Filenames:
        old_file_path=os.path.join(Folder,file_name) # Grab old file path
        file_name=file_name.replace(Old_string,New_string) # Grab old file path and replace old string with new string
        new_file_path=os.path.join(Folder,file_name) # Create new file path with renamed file
        print new_file_path # print new file path progress
        os.rename(old_file_path,new_file_path) # Replace old with new file path
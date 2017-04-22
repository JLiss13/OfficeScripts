#Created by Jordan Liss
# Replace any string in a file name
import os
clear=lambda: os.system('cls') # clear the interpreter console
clear()
# Part1Folder='M:\Engineering\Current_Configuration\MTS_Rails\Downtown (Bayside, C St, Park, Broadway)' # Grab large filepath
# Part2Folder='Track\Civil\LRT 450_Bayside' # Grab part 2 of large filepath
Folder=raw_input("What directory are you working in?") # Must input a string with apostrophes
FileFormat=raw_input("What's the format of file? (.pdf,.dwg,.bak, etc.)")
print FileFormat
Filenames=os.listdir(Folder)
Filenames=filter(lambda k: FileFormat in k, Filenames) # Filters out only strings that have .pdf in it
Prefix=raw_input("What do you want the filenames to have a prefix of?")
print Prefix
index=0
for File_name in Filenames:
        old_file_path=os.path.join(Folder,File_name) # Grab old file path
        New_FileName=Prefix+File_name
        File_name=File_name.replace(File_name,New_FileName) # Grab old file path and replace old string with new string
        new_file_path=os.path.join(Folder,File_name) # Create new file path with renamed file
        print new_file_path # print new file path progress
        os.rename(old_file_path,new_file_path) # Replace old with new file path
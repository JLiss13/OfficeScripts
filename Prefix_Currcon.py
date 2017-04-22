#Created by Jordan Liss
# File Organization Code for SANDAG Currcon Project
import os
# Put folder name as prefix for files
# Part1Folder='M:\Engineering\Current_Configuration\MTS_Rails\Downtown (Bayside, C St, Park, Broadway)'
# Part2Folder='Track\Plan and Profile\LRT 450_Bayside'
FolderPath=raw_input("What directory are you working in?") # Must input a string with apostrophes
print FolderPath
os.chdir(FolderPath)
path,dirs,files=os.walk(FolderPath).next()
number_of_files=len(files)
print number_of_files
Begin=input("What is the number file of the first file? (It includes a directory as a file in the folder)") 
print Begin
End=input("What is the number file of the last file?")
print End
parent_name=raw_input("What do you want the parent name to be?")
for Path, Directories, Filenames in os.walk(FolderPath): # Walk current directory
    # parent_name = os.path.basename(FolderPath) #Get parent name from path
    Filenames=Filenames[Begin-1:End]
    for file_name in Filenames:
        old_file_path=os.path.join(FolderPath,file_name) # Grab old path
        new_file_path =os.path.join(FolderPath, parent_name +'_'+ file_name) #rReplace with new path with directory as prefix
        print "%s ==> %s" % (new_file_path,old_file_path) 
        os.rename(old_file_path, new_file_path) # To remove the Prefix from file names alter here

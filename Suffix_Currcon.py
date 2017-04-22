#Created by Jordan Liss
# Create suffix to order the files according to their respective sheet number
import os
FolderPath=input("What directory are you working in?(Put input in single quotes)") # Must input a string with apostrophes
print FolderPath
Begin=input("What is the number of the first file you want to modify?") # Determine first file to be modified
print Begin
End=input("What is the number of the last file you want to modify?") # Determine last file in sequence to be modified
print End
notation=input("What letter(s) does the drawing number begin with?(Put input in single quotes)") # Must input a string with apostrophes
print notation
firstdnumber=input("What is the beginning drawing number?")  # Set first drawing number
print firstdnumber
lastdnumber=input("What is the last drawing number of the set?")  # Set last drawing number
print lastdnumber
# Path='C:\Users\jli\Dropbox\SANDAG'
for Path, Directories, Filenames in os.walk(FolderPath): # Walk current directory
    Filenames=Filenames[Begin-1:End]
    for file_name in Filenames: # Read current directory
        if firstdnumber <=lastdnumber: # Set last sheetnumber
            suffix=notation +'-'+str(firstdnumber) # 'New' is the letter and sheetnumber of the drawing/sheet number
            old_file_path= os.path.join(FolderPath,file_name) # Grab old path
            new_file_path = os.path.join(FolderPath,file_name[len(file_name)-4:len(file_name)]+'_'+suffix) # Create new file path. Does not place suffix after format extension
            print "%s ==> %s" % (old_file_path,new_file_path) # Print for loop progress
            os.rename(old_file_path,new_file_path) # Rename file paths
            firstdnumber=firstdnumber+1 # sheet number counter
#Created by Jordan Liss
# Replace any string in a file name
# Follow the prompts
import os
clear=lambda: os.system('cls') # clear the interpreter console
clear()
# Part1Folder='M:\Engineering\Current_Configuration\MTS_Rails\Downtown (Bayside, C St, Park, Broadway)' # Grab large filepath
# Part2Folder='Track\Civil\LRT 450_Bayside' # Grab part 2 of large filepath
FolderPath=raw_input("What directory are you working in?") # Must input a string with apostrophes
#FolderPath="M:\Engineering\Current_Configuration\MTS_Rails\Old Town (Santa Fe Depot to Old Town)\Traction Power\Traction Power Substation\Civil\A St TPSS"
Decider=input("Does the string you want to replace have a sequence of numbers? (Yes=1 and No=2)")
if Decider == 1:
    #notation=input("What letter(s) does the drawing number begin with? (Put input in single quotes)") # Must input a string with apostrophes
    # print notation
    firstdnumber=input("What is the beginning drawing number?")  # Set first drawing number
    print firstdnumber
    lastdnumber=input("What is the last drawing number of the set?")  # Set last drawing number
    print lastdnumber 
    # Decider2=input("Do you want to replace string with nothing?(Yes=1 No=2)")
    Filenames=os.listdir(FolderPath)
    Filenames=filter(lambda k: '.pdf' in k, Filenames) # Filters out only strings that have .pdf in it
    # index=[Filenames.index(i) for i in Filenames if str(firstdnumber) in i]
    notation2=raw_input("What texts does the new drawing number begin with?")
    print notation2
    firstdnumber2=input("What is the new beginning drawing number?")  # Set first drawing number
    print firstdnumber2
    for file_name in Filenames:
        print file_name
        firstdnumbertemp=firstdnumber
        firstdnumber2temp=firstdnumber2
        while firstdnumbertemp < lastdnumber+1: # Set last sheetnumber
            old_file_path=os.path.join(FolderPath,file_name)
            Old_string=str(firstdnumbertemp)
            New_string=notation2+str(firstdnumber2temp)
            file_name=file_name.replace(Old_string,New_string)
            new_file_path=os.path.join(FolderPath,file_name) # Create new file path with renamed file
            print new_file_path # print new file path progress
            os.rename(old_file_path,new_file_path) # Replace old with new file path
            firstdnumbertemp=firstdnumbertemp+1
            firstdnumber2temp=firstdnumber2temp+1
            print firstdnumbertemp
elif Decider==2:
    FileFormat=raw_input("What is the file format?")
    Old_string=raw_input("What strings of filename do you want to replace?")
    New_string=raw_input("What do you want the old string to be replaced with?")
    Filenames=os.listdir(FolderPath) # Make list of directory a string array
    Filenames=filter(lambda k: FileFormat in k, Filenames) # Filters out only strings that have .pdf in it
    for file_name in Filenames:
        old_file_path=os.path.join(FolderPath,file_name) # Grab old file path
        file_name=file_name.replace(Old_string,New_string) # Grab old file path and replace old string with new string
        new_file_path=os.path.join(FolderPath,file_name) # Create new file path with renamed file
        print new_file_path # print new file path progress
        os.rename(old_file_path,new_file_path) # Replace old with new file path
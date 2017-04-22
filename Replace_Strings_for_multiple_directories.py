import os
clear=lambda: os.system('cls') # clear the interpreter console
clear()
# Part1Folder='M:\Engineering\Current_Configuration\MTS_Rails\Downtown (Bayside, C St, Park, Broadway)' # Grab large filepath
# Part2Folder='Track\Civil\LRT 450_Bayside' # Grab part 2 of large filepath
# FolderPath=raw_input("What directory are you working in?") # Must input a string with apostrophes
firstdnumber=input("What is the beginning drawing number?")  # Set first drawing number
print firstdnumber
lastdnumber=input("What is the last drawing number of the set?")  # Set last drawing number
print lastdnumber 
notation2=raw_input("What texts does the new drawing number begin with?")
print notation2
firstdnumber2=input("What is the new beginning drawing number?")  # Set first drawing number
print firstdnumber
#Place directory hyperlinks here

#FolderPath1="M:\Engineering\Current_Configuration\MTS_Rails\Old Town (Santa Fe Depot to Old Town)\Traction Power\Traction Power Substation\Circuit Plan\A St TPSS"
#FolderPath2="M:\Engineering\Current_Configuration\MTS_Rails\Yard\Traction Power\Traction Power Substation\Circuit Plan\Yard Shop 1 TPSS"
FolderPath3="M:\Engineering\Current_Configuration\MTS_Rails\East (DT to Baltimore)\Traction Power\Traction Power Substation\Single Line Diagram\Sixty-Fifth St TPSS"
FolderPath4="M:\Engineering\Current_Configuration\MTS_Rails\East (DT to Baltimore)\Traction Power\Traction Power Substation\Single Line Diagram\Twenty-Seventh&Commercial TPSS"
FolderPath5="M:\Engineering\Current_Configuration\MTS_Rails\East (DT to Baltimore)\Traction Power\Traction Power Substation\Single Line Diagram\Market St TPSS"
directories=[FolderPath3,FolderPath4,FolderPath5]
counter=0
directorynum=len(directories)
while counter < directorynum:
    FolderPath=directories[counter]
    Filenames=os.listdir(FolderPath)
    Filenames=filter(lambda k: '.pdf' in k, Filenames) # Filters out only strings that have .pdf in it
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
    counter=counter+1
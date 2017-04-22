import os
clear=lambda: os.system('cls') # clear the interpreter console
clear()
FolderPath=raw_input("What directory are you working in?") # Must input a string with apostrophes
Filenames=os.listdir(FolderPath)
Filenames=filter(lambda k: k.endswith(('.dwg','pdf')), Filenames)
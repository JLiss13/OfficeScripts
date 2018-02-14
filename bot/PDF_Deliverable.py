import os
# Grab PDF
Folderpath_Of_workspace='/Users/Jaliss/Documents/UCSC/CMPE_218/Mechatronics_Book' # Location of PDF Files
Filelist=os.listdir(Folderpath_Of_workspace)
Filelist=filter(lambda k: '.pdf' in k, Filelist)# only files from Filenames list
print Filelist
# Edit PDF

# Merge PDFs
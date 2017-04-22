#Created by Jordan Liss
#Extract pages from .PDF into current directory
import os
import pickle # pickle library to save variables outside of whileloop
from PyPDF2 import PdfFileWriter, PdfFileReader
from CurCon_Module import ExtractFileCategories, PrintToCSVReport, savetext

clear=lambda: os.system('cls') # clear the interpreter console
clear()
infinity =''
savedvalue=[0,0,0,0,0,0,0]
pickle.dump(savedvalue,open("save.p","wb"))
while infinity == '': # infiinite while loop

# Prompts
    FilepathofOriginal=raw_input("What's the PDF to be split?")
    FilepathofOriginal=savetext(FilepathofOriginal,savedvalue,1)
    drawing1=input('Whats the first drawing sheet you want to extract?')
    drawing2=input('Whats the last drawing sheet you want to extract?')
    if drawing1 == drawing2:
        duplicate=''
        # duplicate=raw_input('Is the file a duplicate of the previous individual sheet?(y/ )') 
        if duplicate == 'y': # If there's a duplicate sheet save text from previous sheet
            Engineer_of_record=savedvalue[0]
            FilepathofOriginal=savedvalue[1]
            Filepath=savedvalue[2]
            Drawing_title=savedvalue[3]
            From=savedvalue[4]
            To=savedvalue[5]
            notation=savedvalue[6]
            # notation1='(2)'
        else:
            Engineer_of_record="SIEMENS"
            Engineer_of_record=savetext(Engineer_of_record,savedvalue,0)
            Filepath=raw_input('Destination Filepath?')
            Filepath=savetext(Filepath,savedvalue,2)
            Drawing_title=raw_input('Drawing title?')
            Drawing_title=savetext(Drawing_title,savedvalue,3)
            From=raw_input("From Stationing (Don't forget the +)")
            From=savetext(From,savedvalue,4)
            To=raw_input("To Stationing (Don't forget the +)")
            To=savetext(To,savedvalue,5)
            notation=raw_input("What letter(s) does the new drawing number begin with?")
            notation=savetext(notation,savedvalue,6)
            # notation1=raw_input("What letter(s) does the new drawing number end with?")
            lastdnumber=input("What is the last drawing number?") 
            os.chdir(Filepath) # Change directory
    else:
        Engineer_of_record="SIEMENS"
        Engineer_of_record=savetext(Engineer_of_record,savedvalue,0)
        Filepath=raw_input('Destination Filepath?')
        Filepath=savetext(Filepath,savedvalue,2)
        Drawing_title=' '
        From=' '
        To=' '
        notation=raw_input("What letter(s) does the new drawing number begin with?")
        notation=savetext(notation,savedvalue,6)
        # notation1=raw_input("What letter(s) does the new drawing number end with?")
        lastdnumber=input("What is the last drawing number?") # Set first drawing number # Read PDF
    filenamepdf=file(FilepathofOriginal,'rb')
    inputpdf=PdfFileReader(filenamepdf) # Run through PdfFileReader engine
    os.chdir(Filepath) # Change directory
    firstdnumber=lastdnumber-(drawing2-drawing1)
    # secondnumber=input("What is the last number?")
    
# Record category into hyperlinks.csv, by knowing the filepath directory. 
    
    # If Main category is Track, Signaling or Network Comm.(\Test Data or Agreement and Documents or Assembly)
    Line_segment, Main_cat, Sub_cat, Generalname=ExtractFileCategories(Filepath)
    pickle.dump(savedvalue,open("save.p","wb"))
    
    # Defining temp hyperlink .txt file
    hyperlink_directory='P:\Current_Configuration\MTS_Rails\Metadata Extras\hyperlinks.csv'
    # Extract pages from .PDF into respective destination folder and record transfer to hyperlink.csv file for later import into Metadata File
    while drawing1 <= drawing2: 
        output=PdfFileWriter() # Create new empty PDF sheet
        output.addPage(inputpdf.getPage(drawing1-1)) 
        New_string=notation+str(firstdnumber)+'.pdf' # Modify string name
        NewFilename=os.path.join(Filepath,New_string)

        # Write gathered information to the destination csv file
        additional_line=['=HYPERLINK('+'"'+NewFilename+'"'+','+'"'+New_string+'")'+';'+'6/9/11'+';'+ 'MTS Rail'+';'+ Line_segment+';'+'Segment(Hidden)'+';'+Main_cat+';'+ \
            Sub_cat+';'+'As-Built'+';'+Generalname+';'+notation+str(firstdnumber)+';'+Drawing_title+';'+Engineer_of_record+';'+From+';'+To+'; ; ; ; ; ; ; ; ; ; ;']
        PrintToCSVReport(hyperlink_directory,additional_line) # Prints information to CSVfile
        outputFile=file(NewFilename,'wb') 
        firstdnumber=firstdnumber+1
        print firstdnumber
        # secondnumber=secondnumber+1
        drawing1=drawing1+1
        print drawing1
        with open(NewFilename,'wb'):
            output.write(outputFile)
        outputFile.close()
    filenamepdf.close()
    print savedvalue # print save the saved values from pickle dump
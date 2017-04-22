#Created by Jordan Liss
#Extract pages from .PDF into current directory
import os
import pickle # pickle library to save variables outside of whileloop
from PyPDF2 import PdfFileWriter, PdfFileReader
clear=lambda: os.system('cls') # clear the interpreter console
clear()
infinity =''
savedvalue=[0,0,0,0,0,0]
pickle.dump(savedvalue,open("save.p","wb"))
while infinity == '': # infiinite while loop
    def savetext(inputvalue,savedvalue,index,): #save previous text for the next round of metadata input
        if inputvalue=='s': #Type s into any prompt and the previous input from the previous loop will be the current value
            savedvalue=pickle.load(open("save.p","rb")) # Dump pickle cache into saved variable
            inputvalue=savedvalue[index] #Save previous text to current text
        else:
            savedvalue[index]=inputvalue # Save new text to replace old text
            pickle.dump(savedvalue,open("save.p","wb"))  # save text to forever changing file
        return inputvalue
# Prompts
    FilepathofOriginal='M:\Engineering\Current_Configuration\MTS_Rails\Old Town (Santa Fe Depot to Old Town)\Traction Power\Traction Power Substation\Circuit Plan\A St TPSS\A Street As Built.pdf'
    drawing1=input('Whats the first drawing sheet you want to extract?')
    drawing2=input('Whats the last drawing sheet you want to extract?')
    if drawing1 == drawing2:
        duplicate=raw_input('Is the file a duplicate of the previous individual sheet?(y/ )') 
        if duplicate == 'y': # If there's a duplicate sheet save text from previous sheet
            Engineer_of_record=savedvalue[0]
            Filepath=savedvalue[1]
            Drawing_title=savedvalue[2]
            From=savedvalue[3]
            To=savedvalue[4]
            notation=savedvalue[5]
            # notation1='(2)'
        else:
            Engineer_of_record=raw_input("Who was the Engineer on Record?")
            Engineer_of_record=savetext(Engineer_of_record,savedvalue,0)
            Filepath=raw_input('Destination Filepath?')
            Filepath=savetext(Filepath,savedvalue,1)
            Drawing_title=raw_input('Drawing title?')
            Drawing_title=savetext(Drawing_title,savedvalue,2)
            From=raw_input("From Stationing (Don't forget the +)")
            From=savetext(From,savedvalue,3)
            To=raw_input("To Stationing (Don't forget the +)")
            To=savetext(To,savedvalue,4)
            notation=raw_input("What letter(s) does the new drawing number begin with?")
            notation=savetext(notation,savedvalue,5)
            # notation1=raw_input("What letter(s) does the new drawing number end with?")
            lastdnumber=input("What is the last drawing number?") 
            os.chdir(Filepath) # Change directory
    else:
        Engineer_of_record=raw_input("Who was the Engineer on Record?")
        Engineer_of_record=savetext(Engineer_of_record,savedvalue,0)
        Filepath=raw_input('Destination Filepath?')
        Filepath=savetext(Filepath,savedvalue,1)
        Drawing_title=' '
        From=' '
        To=' '
        notation=raw_input("What letter(s) does the new drawing number begin with?")
        notation=savetext(notation,savedvalue,5)
        # notation1=raw_input("What letter(s) does the new drawing number end with?")
        lastdnumber=input("What is the last drawing number?") # Set first drawing number # Read PDF
    filenamepdf=file(FilepathofOriginal,'rb')
    inputpdf=PdfFileReader(filenamepdf) # Run through PdfFileReader engine
    os.chdir(Filepath) # Change directory
    firstdnumber=lastdnumber-(drawing2-drawing1)
    # secondnumber=input("What is the last number?")
# Record category into hyperlinks.csv, by knowing the filepath directory. 
    # If Main category is Track, Signaling or Network Comm.(\Test Data or Agreement and Documents or Assembly)
    Words_1=["Track","Signaling","Assembly","TestData","AgreementandDocuments"]
    Words_3=["Traction Power","Fiber Cable Plan","Fiber Cabling Schedule","Fiber Splicing Diagram","Single Block Diagram"]
    for item in Words_1:  
        if item in Filepath:
            Pathsplit=os.path.split(Filepath)
            Path_Sub_cat1=os.path.split(Pathsplit[0])
            Sub_cat=Path_Sub_cat1[1]
            Path_Main_cat1=os.path.split(Path_Sub_cat1[0])
            Main_cat=Path_Main_cat1[1]
            Path_Line_segment=os.path.split(Path_Main_cat1[0])
            Line_segment=Path_Line_segment[1]
    # If Main category is Stations
    if "Stations" in Filepath:
        Pathsplit=os.path.split(Filepath)
        Path_Sub_cat2=os.path.split(Pathsplit[0])
        Sub_cat=Path_Sub_cat2[1]
        Path_Main_cat2=os.path.split(Path_Sub_cat2[0])
        Main_cat=Path_Main_cat2[1]
        Path_Station2=os.path.split(Path_Main_cat2[0])
        Path_Line_segment2=os.path.split(Path_Station2[0])
        Line_segment=Path_Line_segment2[1]
    # If Main category is Traction Power or Network Comm.\Network Diagram
    for item in Words_3:
        if item in Filepath:
            Pathsplit3=os.path.split(Filepath)
            Path_Sub_Sub_cat3=os.path.split(Pathsplit3[0])
            Sub_Sub_cat=Path_Sub_Sub_cat3[1]
            Path_Sub_cat3=os.path.split(Path_Sub_Sub_cat3[0])
            Sub_cat=Path_Sub_cat3[1]
            Sub_cat=Sub_cat+'-'+Sub_Sub_cat
            Sub_cat=Sub_cat.replace("Traction Power Substation","TPSS")
            Path_Main_cat3=os.path.split(Path_Sub_cat3[0])
            Main_cat=Path_Main_cat3[1]
            Path_Line_segment=os.path.split(Path_Main_cat3[0])
            Line_segment=Path_Line_segment[1]
            
    Generalname=os.path.split(Filepath)
    pickle.dump(savedvalue,open("save.p","wb"))
    Generalname=Generalname[1]# Extract Title of File
    # Defining temp hyperlink .txt file
    hyperlink_directory='M:\Engineering\Current_Configuration\MTS_Rails\hyperlinks.csv' 
    # Extract pages from .PDF into respective destination folder and record transfer to hyperlink.csv file for later import into Metadata File
    while drawing1 <= drawing2: 
        output=PdfFileWriter() # Create new empty PDF sheet
        output.addPage(inputpdf.getPage(drawing1-1)) 
        New_string=Generalname+'_'+notation+str(firstdnumber)+'.pdf' # Modify string name
        NewFilename=os.path.join(Filepath,New_string)
        all_content=[]
        with open(hyperlink_directory) as f:
            all_lines = [line.strip() for line in f]
            all_content+=all_lines #aka all_content = all_content+ all_lines
        # Write gathered information to the destination csv file
        additional_line=['=HYPERLINK('+'"'+NewFilename+'"'+','+'"'+New_string+'")'+';'+'6/9/14'+';'+ 'MTS Rail'+';'+ Line_segment+';'+'Segment(Hidden)'+';'+Main_cat+';'+ \
            Sub_cat+';'+'As-Built'+';'+Generalname+';'+notation+str(firstdnumber)+';'+Drawing_title+';'+Engineer_of_record+';'+From+';'+To+'; ; ; ; ; ; ; ; ; ; ;']
        all_content+=additional_line                                           # took out notation1
        with open(hyperlink_directory, 'w') as f: # 'w'=Write permissions to file
            for line in all_content:
                print >> f, line # Inserts line of appended array to each new line of hyperlink.csv file
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
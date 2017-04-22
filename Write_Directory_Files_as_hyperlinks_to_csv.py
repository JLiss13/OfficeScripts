#For write hyperlinks in a directory to a .csv or .txt
import os 
clear=lambda: os.system('cls') # clear the interpreter console
clear()
Filepath=raw_input('Destination Filepath?')
filetype=raw_input('What kind of file type are you looking for? (.pdf, .dwg, etc.)')
Contract_Name=raw_input('What is the contract name?')
#Name=raw_input('Common name found in title? (Plus any underscores or blanks after)')
#Name="Yard Shop 1 TPSS_"
hyperlink_directory='M:\Engineering\Current_Configuration\MTS_Rails\Metadata Extras\hyperlinksfromdirectory.csv'
Files=os.listdir(Filepath)
Files=filter(lambda k: k.endswith(('.dwg','pdf')), Files) # Filters out only strings that have .dwg
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
filenum=0
while filenum <len(Files):
    all_content=[]
    with open(hyperlink_directory) as f:
        all_lines = [line.strip() for line in f]
        all_content+=all_lines #aka all_content = all_content+ all_lines
    # Write gathered information to the destination csv file
    Individual_Filepaths=os.path.join(Filepath,Files[filenum])
    Individual_File=Files[filenum]
    Drawing_number=Individual_File[Individual_File.find(filetype)] # Grab the drawing title and not filetype
    additional_line=['=HYPERLINK('+'"'+ Individual_Filepaths +'"'+','+'"'+Individual_File+'")'+';'+';'+'12/11'+';'+ 'MTS Rail'+';'+ Line_segment +';'+'Segment(Hidden)'+';'+Main_cat+';'+ \
        Sub_cat+';'+'As-Built'+';'+Contract_Name+';'+Drawing_number+';'+'Drawing Title'+';'+'SIEMENS'+'; ; ; ; ; ; ; ; ; ; ; ; ; ;']
    all_content+=additional_line
    filenum=filenum+1
    with open(hyperlink_directory, 'w') as f: # 'w'=Write permissions to file
        for line in all_content:
            print >> f, line # Inserts line of appended array to each new line of hyperlink.csv file
    

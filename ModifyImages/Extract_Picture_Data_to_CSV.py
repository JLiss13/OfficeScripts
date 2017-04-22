import os
from PIL import Image,ExifTags
clear=lambda: os.system('cls') # clear the interpreter console
clear()
Folder=raw_input("What directory are you working in?")
# FileFormat=raw_input("What's the format of file? (.pdf,.dwg,.bak,.jpg etc.)")
FileFormat='.JPG'
Name=raw_input('Common name found in title of each drawing?') #Name is used to extract Picture Number (See Line 54)
print FileFormat
Filenames=os.listdir(Folder)
Filenames=filter(lambda k: FileFormat in k, Filenames)# only files from Filenames list

# Write Metatags of photo to CSV to be imported into Excel
filenum=0
Catenary_Pictures_data='C:\Users\jli\Documents\Side Projects\Dale\Catenary\Catenary_Pictures_data.csv'
while filenum <len(Filenames):
    all_content=[]
    with open(Catenary_Pictures_data) as f:
        all_lines = [line.strip() for line in f]
        all_content+=all_lines #aka all_content = all_content+ all_lines
        
    # Write gathered information to the destination csv file
    imgpath=os.path.join(Folder,Filenames[filenum])
    img=Image.open(imgpath) # open image file
    exif={ #Extract metadata into dictionary
        ExifTags.TAGS[k]:v
        for k,v in img._getexif().items()
        if k in ExifTags.TAGS
    }
    # Convert Degrees Minutes Seconds to Decimal Degrees
    lat = [float(x)/float(y) for x, y in exif['GPSInfo'][2]]
    latref = exif['GPSInfo'][1]
    lon = [float(x)/float(y) for x, y in exif['GPSInfo'][4]]
    lonref = exif['GPSInfo'][3]

    lat = lat[0] + lat[1]/60 + lat[2]/3600
    lon = lon[0] + lon[1]/60 + lon[2]/3600
    if latref == 'S':
        lat = -lat
    if lonref == 'W':
        lon = -lon
    #exif_data=img._getexif()
    print lat
    print lon
    # Grab date and time  metadata
    Datetime=exif['DateTime']
    Datetime=Datetime.encode('ascii','ignore')
    Date=Datetime[0:10]
    Time=Datetime[11:len(Datetime)]
    
    #Write to csv file Catenary Pictures data
    Individual_Filepaths=os.path.join(Folder,Filenames[filenum])
    Individual_File=Filenames[filenum]
    Picture_number=Individual_File[len(Name):Individual_File.find(".JPG")] # Grab the drawing number
    additional_line=['=HYPERLINK('+'"'+ Individual_Filepaths +'"'+','+'"'+Individual_File+'")'+';'+'Photo Subject'+';'+ Name +';'+ Picture_number+';'+Date+';'+Time+';'+str(lat)+';'+str(lon)]
    all_content+=additional_line
    filenum=filenum+1
    with open(Catenary_Pictures_data, 'w') as f: # 'w'=Write permissions to file
        for line in all_content:
            print >> f, line # Inserts line of appended array to each new line of hyperlink.csv file
    
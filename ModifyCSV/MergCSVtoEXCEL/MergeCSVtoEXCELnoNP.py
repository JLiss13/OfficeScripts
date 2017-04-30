# Automate the merging of .csv files into the xls format you want
# For more information on how I created the script please visit
# https://xlsxwriter.readthedocs.io/working_with_pandas.html or my github account
import os
import pandas as pd
from openpyxl import Workbook
dir=input("What is the root directory where the data server health files are?")
# dir="/Users/Jaliss/Documents/UCSC/BELS/DataServersEnergyEfficiency/CommBuildingEnergyData/outputs"
finalfilename=input("What do you want the final excel workbook to be called?")
# finalfilename='comm_data_2017_02'
# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter(finalfilename + '.xlsx', engine='xlsxwriter')
folderlist=os.listdir(dir)
folderlist = filter(lambda k: not '.' in k, folderlist)
folderlist = filter(lambda k: not 'outputs' in k, folderlist)
folderlist = list(filter(lambda k: not '_HOST_' in k, folderlist))
for folder in folderlist:
    print("Folder name " + folder + "--------------------------------------")
    for root, dirs, files in os.walk(os.path.join(dir,folder)):
    # On each iteration the files will be a list of files in the root directory
        files = filter(lambda k: not '.' in k, files)
        files = filter(lambda k: not '_HOST_' in k, files)
        files = list(files)
        csvarray = pd.read_csv(os.path.join(root,files[0]), sep = " ", header = 1,
                    names = ["UnixTimeStamp", files[0]])
        sizefilesarray=len(files)
        for filename in files[1:sizefilesarray]:
            print(filename)
            tempcsvarray = pd.read_csv(os.path.join(root,filename), sep = " ", header = 1,
                                       names = ["UnixTimeStamp", filename])
            csvarray=csvarray.merge(tempcsvarray,on = "UnixTimeStamp",how = "left")
            # print("Size of the tempcsvarray: " + str(tempcsvarray.shape))
            # print("Size of the csvarray: " + str(csvarray.shape))
    # print(type(csvarray)
    # csvarray['UnixTimeStamp'] = csvarray['UnixTimeStamp'].str.replace(':','') #http://stackoverflow.com/questions/14345739/replacing-part-of-string-in-python-pandas-dataframe
    csvarray['UnixTimeStamp'] = csvarray['UnixTimeStamp'].replace(to_replace=':', value='', regex=True)
    csvarray['UnixTimeStamp'] = pd.to_datetime(csvarray['UnixTimeStamp'], unit='s')
    # csvarray.drop(csvarray.columns[0]) #http://stackoverflow.com/questions/13411544/delete-column-from-pandas-dataframe
    csvarray.to_csv(folder + ".csv", sep=',') #http://stackoverflow.com/questions/16923281/pandas-writing-dataframe-to-csv-file
    print("Printed " + folder+".csv ... ")
    print("Shape of " + folder+".csv is " + str(csvarray.shape))

    # Add each merged csvarray to a different worksheet in excel workbook
    # https://xlsxwriter.readthedocs.io/working_with_pandas.html
    # Convert the dataframe to an XlsxWriter Excel object.
    csvarray.to_excel(writer, sheet_name=folder)

# Close the Pandas Excel writer and output the Excel file.
writer.save()
def FindMissingFiles(Filepath,csvfile):
    import os 
    clear=lambda: os.system('cls') # clear the interpreter console
    clear()
    Files=os.listdir(Filepath)
    #CSVtoCompare=raw_input("What's the CSV file to compare with?")
    all_content_CSV=[]
    with open(csvfile) as data_file:
        for line in data_file:
            all_content_CSV.append(line.strip().split(','))
    counter=0
    filesAlreadyFiled=[]
    filesNotFiled=[]
    for filename in Files:
        if any(filename in lines for lines in all_content_CSV):
            filesAlreadyFiled.append(filename)
        else:
            filesNotFiled.append(filename)
    return (filesAlreadyFiled, filesNotFiled)
        
        

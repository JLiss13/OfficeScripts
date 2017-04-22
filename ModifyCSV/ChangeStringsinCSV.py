# Change the strings in a CSV file
import os
hyperlink_directory=raw_input("What's the file directory?")
old_string=raw_input("What's the string that needs to be replaced?")
new_string=raw_input("What's the string it will replace?")
all_content=[]
with open(hyperlink_directory) as f:
    all_lines = [line.strip() for line in f]
    all_content+=all_lines #aka all_content = all_content+ all_lines
    index=0
    for line in all_content:
        all_content[index]=line.replace(old_string,new_string)
        index=index+1
with open(hyperlink_directory, 'w') as f: # f is a temporary variable. 'w'=Write permissions to file
    for line in all_content:
        print >> f, line
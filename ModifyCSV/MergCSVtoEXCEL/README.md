# MergeCSVsinDirectories2EXCELWorkbook

If you are reading this you are in need of putting all .CSV files from different directories into one specific excel workbook. All .csv files in one directory will be merged together based on timestamps to create one .csv larger file and then one worksheet in the single excel workbook. The worksheet title will be the name of the directory.

## Getting Started

1. Download the repo and save it to anywhere you like
2. Make sure you have proper python dependencies installed
3. Run python code, it will prompt you

### Prerequisites

1. [Pandas](http://pandas.pydata.org/getpandas.html)
If you have a mac, open up the terminal and type in "pip install pandas"
Otherwise you will need to download it using the instructions found on the link.

### Installing

1. Look to Getting Started and Prerequisites step 1 

## Running the tests

If you have the code running correctly the code will prompt you:

*What is the root directory where the data server health files are?*

Type in [ROOT DIRECTORY OF .CSV FILES] There's no need for quotations.

*What to do you want the final excel workbook to be called?*

Type in name of the final excel workbook you want it to be.

If run successfully you should get something like this:

*Folder name FIRST DIRECTORY-------------------------------*

*[LIST OF .CSV or .txt files]*

*Printed [LARGEMERGEDCSVFILE]*

*Shape of [LARGEMERGEDCSVFILE] is ([SHAPE])*

*Folder name SECOND DIRECTORY-------------------------------*

## Deployment

Obviously trying this on different machines, different problems can occur. Have no fear google will be your best friend to solve any of those quirks.

## Built With

* [Python](https://www.python.org/)


## Authors

* **Jordan Liss** [Jliss13](https://github.com/JLiss13)

## Acknowledgments

* Hat tip to many of the solutions I found on StackOverflow.


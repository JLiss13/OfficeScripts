from pypdfocr import*
#Created by Jordan Liss
import os
from pyPdf import PdfFileWriter, PdfFileReader
FilepathofOriginal='M:\Engineering\Drawing Inventory\Drawings to be filed\LRT-426.1\LRT 450'
os.chdir(FilepathofOriginal)
Filename='LRT 450_Bayside.pdf'#Name of large pdf file
Filename=file(Filename,'rb')
from pytesser import*
import os
from PIL import*
path=raw_input('New directory?')
os.chdir(path)
imagefile=raw_input('name of imagefile?')
image=Image.open(imagefile)
text=image_to_string(image)
print text
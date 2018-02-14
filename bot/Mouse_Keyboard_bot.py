import matplotlib.pyplot as plt, numpy,os, pyautogui, time, datetime
from PIL import Image 
plt.close('all')
#TESTs
'''
x=400; y=500;
position=pyautogui.position();  # current mouse x and y
print(position);
screen_size=pyautogui.size();  # current screen resolution width and height
print(screen_size);
pyautogui.onScreen(x, y);  # True if x & y are within the screen.
num_seconds=3;
pyautogui.moveTo(x, y, duration=num_seconds)  # move mouse to XY coordinates over num_second seconds
xOffset=100; yOffset=100;
pyautogui.moveRel(xOffset, yOffset, duration=num_seconds)  # move mouse relative to its current position
'''
'''
#Evaluating Screen Resolution and Website
Folderpath_Of_workspace='/Users/Jaliss/Documents/UCSC/CMPE_218/Mechatronics_Book/Screenshots' # Location of TIFF files
os.chdir(Folderpath_Of_workspace)
Filelist=os.listdir(Folderpath_Of_workspace)
Filelist=filter(lambda k: '.tiff' in k, Filelist)# only files from Filenames list
drawing_num=0
for nameOtiff in Filelist:
    nameOtiff=Filelist[drawing_num]
    print nameOtiff
    im = Image.open(nameOtiff) # Use PIL to convert image to image array
    imarray=numpy.asarray(im) # Turn image into array
    plt.figure()
    plt.imshow(imarray)
    plt.show()
    drawing_num=drawing_num+1
'''
#Navigating to Chrome
num_seconds=0.5
pyautogui.moveTo(337, 810, duration=num_seconds) # Make Taskbar Appear
time.sleep(1)
num_seconds=1
pyautogui.click(337, 760, duration=num_seconds) # Click Chrome to open
numberofpages=882
page=782
for page in range(page, numberofpages):
    #Download State
    #Step 1: Clicking Print Icon
    time.sleep(3)
    num_seconds=2
    pyautogui.moveTo(650,400, duration=num_seconds)
    time.sleep(3)
    num_seconds=2
    pyautogui.moveTo(1107,700, duration=num_seconds)
    time.sleep(1)
    num_seconds=0.5
    pyautogui.click(1107,700, duration=num_seconds)
    
    #Step 2: Clicking the Print Button
    time.sleep(3)
    num_seconds=2
    pyautogui.click(730,460, duration=num_seconds)
    
    #Step 3: Clicking Save
    time.sleep(10)
    pyautogui.press('enter')
    
    #Step 4: Changing File Name
    time.sleep(7)
    pyautogui.typewrite(str(page))
    time.sleep(2)
    pyautogui.press('enter')
    
    #Step 5: Clicking the next arrow
    time.sleep(8)
    num_seconds=2
    pyautogui.moveTo(1245,387, duration=num_seconds)
    num_seconds=1
    pyautogui.click(1245,387, duration=num_seconds)
    page=page+1
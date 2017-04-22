import win32com.client,os
directory='C:\Program Files\Autodesk\AutoCAD LT 2015'
os.chdir(directory)
# os.system("acadlt.exe")
acad = win32com.client.Dispatch("acadlt.Application")
doc = acad.ActiveDocument  # Document object 
# iterate trough all objects (entities) in the currently opened drawing
# and if its a BlockReference, display its attributes and some other things.
for entity in acad.ActiveDocument.ModelSpace:
    name = entity.EntityName
    if name == 'AcDbBlockReference':
        HasAttributes = entity.HasAttributes
        if HasAttributes:
            print(entity.Name)
            print(entity.Layer)
            print(entity.ObjectID)
            for attrib in entity.GetAttributes():
                print("  {}: {}".format(attrib.TagString, attrib.TextString))
                # update text
                attrib.TextString = 'modified with python'
                attrib.Update()
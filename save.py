import pickle
def save(inputvalue,index):
    if inputvalue=='s':
        savedvalue=pickle.load(open("save.p","rb"))
        savedvalue[index]
    else:
        inputvalue=inputvalue
        savedvalue[index]=inputvalue
        pickle.dump(savedvalue,open("save.p","wb"))
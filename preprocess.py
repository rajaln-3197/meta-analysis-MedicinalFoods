import glob 
import os
#preprocess for glove
def preprocess():
    os.chdir('D:/Grad/597/Project/code/TXT')
    for filename in glob.glob('./*.txt'):
        f = open(filename,'r',encoding="utf8")
        data = f.readlines()
        content = str('')
        for x in data:
            content = content + str(x) +' '
        data = content
        data = data.replace('\n',' ')
        data = data.replace('[',' ')
        data = data.replace(']',' ')
        data = data.replace("'",' ')
        data = data.replace("'",' ')
        data = data.replace(",",' ')
        fo = open(filename,'w',encoding="utf8")
        fo.write(data)
        f.close()
        fo.close()
#uncomment for glove
#preprocess()
def appendfiles():
    out = open('val.txt','a',encoding="utf8")
    os.chdir('D:/Grad/597/Project/code/VAL')
    for filename in glob.glob('./*.txt'):
        f = open(filename,'r',encoding="utf8")
        #for spacy
        for x in f.readlines():
            out.write(str(x)) 
        #for glove
        #out.write(str(f.readline()))
        f.close()
    out.close()
appendfiles()
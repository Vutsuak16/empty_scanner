import os

path="C:\\Users\windows 7\Desktop\Flask_Upload"

files=os.listdir(path)

for file in files:
    if os.stat(path+"\\"+file).st_size==0:
        os.remove(path+"\\"+file)
import os
def put_path(path):
    files = os.listdir(path)
    for file in files:
        if os.stat(path + "\\" + file).st_size == 0:
            os.remove(path + "\\" + file)

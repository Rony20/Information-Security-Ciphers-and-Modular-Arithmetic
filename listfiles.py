import os
from os import walk

root = 'D:\\CP-SEM_6\\IS'

def list_all(path):
    files = os.listdir(path)
    for file in files:
        low_path = os.path.join(path,file)
        print(low_path)
        if os.path.isdir(low_path):
            list_all(low_path)
        else:
            print(file)

list_all(root)
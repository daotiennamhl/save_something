# import 
import os
from time import sleep

# var
directory = r'C:\Users\daotiennam\Desktop\img'

# function 
def rename_list_path(listdir, somethingweird = ''):
    for i in range(len(listdir)):
        old_path = listdir[i]
        if os.path.isdir(old_path):
            new_path = directory + '\\' + str(i)
        else: 
            new_path = directory + f'\\{somethingweird}' + str(i) + os.path.splitext(old_path)[-1]
        os.rename(old_path, new_path)

# get list images path
listdir = [os.path.join(directory, f) for f in os.listdir(directory)]

# change all file path to new weird path
rename_list_path(listdir, '2#(2Hf()')
print('done step 1!')
sleep(3)

# change file path in to ordered number
listdir = [os.path.join(directory, f) for f in os.listdir(directory)]
rename_list_path(listdir)
print('rename success!')

"""
This snippet code rename all FILE or FOLDER in a folder to new ordered paths
if file: keep the file extension
"""
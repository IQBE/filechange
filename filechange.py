"""
=====================================
by Ilya Quateau
=====================================

"""

import os
import glob

def read(file, rLine = False, line = [1]):
    try:
        if rLine == False:
            f = open(file, "r")
            f.read()
        else:
            f = open(file, "r")
            content = f.readlines()
            for i in line:
                print(content[i - 1])
                
    except:
        print("ERROR: File not found or unreadable!")
    finally:
        f.close()

def write(file, text = "", mode = "w"):
    try:
        if mode == "x" or text == "":
            f = open(file, "x")
            print("SUCCES: Succesfuly made an empty file {}!".format(file))
        elif mode == "w":
            f = open(file, "w")
            f.write(text)
            print("SUCCES: Succesfuly overwritten {} to {}!".format(text, file))
        elif mode == "a":
            f = open(file, "a")
            f.write(text)
            print("SUCCES: Succesfuly appended {} to {}!".format(text, file))
        else:
            print("ERROR: Mode {} is not a valid mode. Choose between 'w', 'a' and 'x'.".format(mode))
    except:
        print("ERROR: Unable to edit file!")
    finally:
        f.close()

def dir(dirName, multi = False):
    if multi == False:
        if not os.path.exists(dirName):
            os.mkdir(dirName)
            print("SUCCES: Directory " , dirName ,  " created!")
        else:    
            print("ERROR: Directory " , dirName ,  " already exists!")
    else: 
        if not os.path.exists(dirName):
            os.makedirs(dirName)
            print("SUCCES: Path " , dirName ,  " created!")
        else:    
            print("ERROR: Path " , dirName ,  " already exists!") 

def delete(file, sort = "file" , rec = True):
    if sort == "file":
        files = glob.glob(file, recursive = rec)

        for f in files:
            try:
                os.remove(f)
                print("SUCCES: Succesfuly removed file {}!".format(file))
            except OSError as e:
                print("ERROR: {}: {}".format(file, e.strerror))
    else:
        dir_path = file
        
        try:
            os.rmdir(dir_path)
            print("SUCCES: Succesfuly removed directory {}!".format(dir_path))
        except OSError as e:
            print("ERROR: {}: {}".format(dir_path, e.strerror))
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author : microfat
# @time   : 07/28/21 11:04:11
# @File   : setup_win.py

import os
from distutils.core import setup
from Cython.Build import cythonize


def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        elif os.path.splitext(fullPath)[-1] == '.py':
            allFiles.append(fullPath)

    return allFiles

def getAllFiles(dirNames):
    all = list()
    for dir_name in dirNames:
       all.extend(getListOfFiles(dir_name))
    return all

listOfFiles = getAllFiles(['module', 'models', 'controllers'])

for file in listOfFiles:
    setup(ext_modules=cythonize(file, language_level = "3"))
    path = os.path.splitext(file)[0].replace('/', '\\')
    print(os.system(f'del {path}.*'))
    print(os.system(f'move *.pyd {os.path.split(file)[0]}'))
print(os.system('rmdir /s /q build'))

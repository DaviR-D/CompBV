import shutil
import os

def copy(resultList, folderList):
    cont = 0
    if resultList != []:
        for file in resultList:
            dir = folderList[cont]
            shutil.copy2(file, dir)
            cont += 1
        cont = 0

def delete(resultList):
    for file in resultList:
        os.remove(file)

import shutil
import os

def copy(result_list_cache, folder_list_cache):
    cont = 0
    if result_list_cache != []:
        for file in result_list_cache:
            dir = folder_list_cache[cont]
            shutil.copy2(file, dir)
            cont += 1
        cont = 0

def delete(result_list_cache):
    for file in result_list_cache:
        os.remove(file)

from threading import Thread
import os.path
import glob
import os

resultListCache = list()
folderListCache = list()

# Função que chama as outras e inicia as threads
def folderManager(folder1, folder2, clean=0):
    global resultListCache
    global folderListCache

    if (clean):
        resultListCache = list()
        folderListCache = list()


    fileList1, path1, dirList1 = loadFiles(folder1)
    fileList2, path2, dirList2 = loadFiles(folder2)

    compFolders(dirList1, dirList2)

    comp1 = Thread(target = compFiles, args = (fileList1, fileList2, path1, folder2))
    comp2 = Thread(target = compFiles, args = (fileList2, fileList1, path2, folder1))

    comp1.start()
    comp2.start()

    comp1.join()
    comp2.join()

    return resultListCache, folderListCache

# Copara as duas pastas e armazena a diferença entre elas
def compFiles(fileList1, fileList2, path1, path2):
    global resultListCache
    global folderListCache
    x = True
    for f, path in zip(fileList1, path1):
        for a in (fileList2):
            if f == a:
                x = False
            if not x: break
        if x:
            print(path)
            resultListCache.append(path)
            folderListCache.append(path2)
        x = True

# Armazena o tamanho dos arquivos em bytes em listas para que as pastas possam ser comparadas simultâneamente
def loadFiles(folder):
    sizesList = list()
    path = list()
    dirList = list()


    for f in glob.glob(folder + '/*'):
        if not os.path.isdir(f):
            sizesList.append(os.path.getsize(f))
            path.append(f)
        else:
            dirList.append(f)

    dirList.sort()

    return sizesList, path, dirList

# Verifica se as subpastas são de mesmo nome e se sim, as envia para a função principal para serem comparadas também
def compFolders(dirList1, dirList2):
    for l1 in dirList1:
        for l2 in dirList2:
            if os.path.basename(l1) == os.path.basename(l2):
                folderManager(l1, l2)

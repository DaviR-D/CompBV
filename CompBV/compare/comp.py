from threading import Thread
import os.path
import glob
import os

resultListCache = []
folderListCache = []

# Função que chama as outras e inicia as threads
def folderManager(folder1, folder2):
    global resultListCache
    global folderListCache

    fileList1, fileList2, path1, path2 = loadFiles(folder1, folder2)
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
            resultListCache += [path]
            folderListCache += [path2]
        x = True

# Armazena o tamanho dos arquivos em bytes em listas para que as pastas possam ser comparadas simultâneamente
def loadFiles(folder1, folder2):
    sizesList1 = []
    sizesList2 = []
    path1 = []
    path2 = []
    dirList1 = []
    dirList2 = []

    for f in glob.glob(folder1 + '/*'):
        if not os.path.isdir(f):
            sizesList1 = sizesList1 + [os.path.getsize(f)]
            path1 = path1 + [f]
        else:
            dirList1 = dirList1 + [f]

    for f in glob.glob(folder2 + '/*'):
        if not os.path.isdir(f):
            sizesList2 = sizesList2 + [os.path.getsize(f)]
            path2 = path2 + [f]
        else:
            dirList2 = dirList2 + [f]

    dirList1.sort()
    dirList2.sort()

# Verifica se as subpastas são de mesmo nome e se sim, as envia para a função principal para serem comparadas também
    for l1, l2 in zip(dirList1, dirList2):
        if os.path.basename(l1) == os.path.basename(l2):
            folderManager(l1, l2)

    return sizesList1, sizesList2, path1, path2

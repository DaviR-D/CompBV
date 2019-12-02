import os.path
import glob
import os

result_list_cache = []
folder_list_cache = []

def compFolders(f1,f2):
    global result_list_cache
    global folder_list_cache
    result_list_cache = []
    folder_list_cache = []
    #Efetivando a checagem dos
    compFiles(f1,f2) #arquivos de
    compFiles(f2,f1) #ambas as pastas
    return result_list_cache, folder_list_cache


def compFiles(f1,f2):
    global result_list_cache
    global folder_list_cache
    x = True #Variável de controle
    for f in glob.glob(f1 + '/*'): #Um arquivos da primeira pasta
        for a in glob.glob(f2 + '/*'): #É comparado com todos da segunda
            if dirComp(f,a): continue #Caso retorne verdadeiro passamos para o próximo loop
            if os.path.getsize(f) == os.path.getsize(a) and not os.path.isdir(f): #Se os dois arquivos forem iguais
                x = False #(mesmo tamanho em bytes), x se torna falso
            if not x: break #e o segundo loop é parado, passando para o próximo arquivo a ser testado
        if x and not os.path.isdir(f): #Se não foi encontrado nenhum arquivo
            print(f) #igual a "f" na segunda pasta e "f" não for diretório
            result_list_cache += [f] #Adiciona o endereço de "f" na lista de arquivos a serem copiados
            folder_list_cache += [f2] #Identifica a pasta para qual o arquivo deve ir
        x = True #x volta a ser verdadeiro

def dirComp(f,a): #Verifica se um dos endereços não é uma pasta
    if os.path.isdir(f) and os.path.isdir(a) and os.path.basename(f) == os.path.basename(a): #Se os dois endereços
        compFiles(f,a) #forem subpastas de mesmo nome, compara as diferenças dos dois
        return True # retorna verdadeiro
    elif os.path.isdir(f) or os.path.isdir(a): #se só um deles dor pasta ou não tiverem
        return True #nomes iguais, apenas retorna verdadeiro
    else: #caso contrário, apenas retorna
        return

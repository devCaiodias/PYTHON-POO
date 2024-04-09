# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

caminho = os.path.join(r'C:\\Users', 'caiod', 'pythonPOO', 'modulosPy')
counter = count()

for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)
    
    for dir_ in dirs:
        print('    ',the_counter, 'Dir: ', dir_)
        
    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        print('        ',the_counter, 'File: ', caminho_completo_arquivo)
        
        # N execute esse comando (VAI APAGAR TUDO DA PASTA)
        # os.unlink(caminho_completo_arquivo)
        
        
        
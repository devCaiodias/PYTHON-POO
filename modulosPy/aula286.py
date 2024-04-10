# os + shutil - Copiando arquivos com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy


# import os
# import shutil
# # C:\Users\caiod\pythonPOO\modulosPy c:\Users\caiod\exemplopy
# HOME = os.path.expanduser('~')
# DESKTOP = os.path.join(HOME, 'Desktop')
# PASTA_ORIGINAL = os.path.join(DESKTOP, 'exemplopy')
# NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')


# os.makedirs(NOVA_PASTA, exist_ok=True)

# for root, dirs, files in os.walk(PASTA_ORIGINAL):
#     for dir_ in dirs:
#         caminho_novo_diretorio = os.path.join(
#             root.replace( PASTA_ORIGINAL, NOVA_PASTA), dir_
#         )
#         # print(caminho_novo_diretorio)
#         os.makedirs(caminho_novo_diretorio, exist_ok=True)
        
#     for file in files:
#         caminho_file = os.path.join(root, file)
#         caminho_novo = os.path.join(
#             root.replace( PASTA_ORIGINAL, NOVA_PASTA), file
#         )
#         shutil.copy(caminho_file, caminho_novo)
        

# os + shutil - Apagando, copiando, movendo e renomeando pastas com Python
# Vamos copiar arquivos de uma pasta para outra.
# Copiar -> shutil.copy
# Copiar Árvore recursivamente -> shutil.copytree
# Apagar Árvore recursivamente -> shutil.rmtree
# Apagar arquivos -> os.unlink
# Renomear/Mover -> shutil.move ou os.rename

import os
import shutil
# C:\Users\caiod\pythonPOO\modulosPy c:\Users\caiod\exemplopy
HOME = os.path.expanduser('~')
DESKTOP = os.path.join(HOME, 'Desktop')
PASTA_ORIGINAL = os.path.join(DESKTOP, 'exemplopy')
NOVA_PASTA = os.path.join(DESKTOP, 'NOVA_PASTA')

shutil.rmtree(NOVA_PASTA, ignore_errors=True)
shutil.copytree(PASTA_ORIGINAL, NOVA_PASTA)
# shutil.rmtree(NOVA_PASTA, ignore_errors=True)

# shutil.move(NOVA_PASTA, NOVA_PASTA + '_EITA')
# shutil.rmtree('C:\\Users\\caiod\\pythonPOO\\_EITA', ignore_errors=True)
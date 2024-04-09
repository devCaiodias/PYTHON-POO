# os.listdir para navegar em caminhos
# /Users/luizotavio/Desktop/EXEMPLO
# C:\Users\luizotavio\Desktop\EXEMPLO
# caminho = r'C:\\Users\\luizotavio\\Desktop\\EXEMPLO'
import os

# C:\Users\caiod\pythonPOO\modulosPy
caminho = os.path.join(r'C:\\Users', 'caiod', 'pythonPOO', 'modulosPy')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print(pasta)
    
    # continue
    if not os.path.isdir(caminho_completo_pasta):
        continue
    
    for item in os.listdir(caminho_completo_pasta):
        print('   ',item)
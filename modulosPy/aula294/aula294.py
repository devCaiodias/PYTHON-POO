# csv.writer e csv.DictWriter para escrever em CSV
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário

import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula294.csv'

lista_cliente = [
    {'Nome': 'Caio Dias', 'Endereco': 'AV 1, 22'},
    {'Nome': 'Vini Mendz', 'Endereco': 'R. 2, "1"'},
    {'Nome': 'Joao barro', 'Endereco': 'AV b, 3A'}
]

# EM DICIONARIOOO
with open(CAMINHO_CSV, 'w') as file:
    nome_colunas = lista_cliente[0].keys()
    escritor = csv.DictWriter(file,fieldnames=nome_colunas)
    
    escritor.writeheader()
    
    for cliente in lista_cliente:
        print(cliente)
        escritor.writerow(cliente)



# EM LISTAAAA

# with open(CAMINHO_CSV, 'w') as file:
#     colunas = lista_cliente[0].keys()
#     escritor = csv.writer(file)

#     escritor.writerow(colunas)
    
#     for cliente in lista_cliente:
#         escritor.writerow(cliente.values())
    
# print(lista_cliente[0].values())
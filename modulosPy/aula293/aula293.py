# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'aula293.csv'
print(CAMINHO_CSV)

# with open(CAMINHO_CSV, 'r') as file:
#     leitor = csv.reader(file)
    
#     for linha in leitor:
#         print(linha)

with open(CAMINHO_CSV, 'r') as file:
    leitor = csv.DictReader(file)
    
    for linha in leitor:
        print(linha['Nome'])
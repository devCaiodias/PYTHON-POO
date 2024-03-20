import json
from ex206 import caminho__arquivo, Pessoa, fazer_dump

with open(caminho__arquivo, 'r', encoding='utf8') as file:
    dados = json.load(file)
    p1 = Pessoa(**dados[0])
    p2 = Pessoa(**dados[1])
    p3 = Pessoa(**dados[2])
    
    print(p1.nome, p1.idade)
    print(p2.nome, p2.idade)
    print(p3.nome, p3.idade)
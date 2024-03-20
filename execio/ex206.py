# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

caminho__arquivo = 'C:\\Users\\caiod\\pythonPOO\\execio\\'
caminho__arquivo += 'json206.json'

p1 = Pessoa('Caio', 18)
p2 = Pessoa('Vini', 20)
p3 = Pessoa('João', 19)
dados = [vars(p1), vars(p2), vars(p3)]

def fazer_dump():
    with open(caminho__arquivo, 'w', encoding='utf8' ) as file:
        json.dump(dados, 
                file,
                indent=2,
                ensure_ascii=False
                )
        
if __name__ == '__main__':
    print('Ele é o __main__')
    fazer_dump()
# Atributos de classe

class Pessoa:
    ano_atual = 2024
    
    def __init__(self,nome, idade):
        self.nome = nome
        self.idade = idade
        
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

print('P1: ')    
p1 = Pessoa('Caio', 18)
print(p1.nome)
print(p1.idade)
print(p1.get_ano_nascimento())

print()

print('P2: ')
p2 = Pessoa('Vini', 20)
print(p2.nome)
print(p2.idade)
print(p2.get_ano_nascimento())
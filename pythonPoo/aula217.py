# Herança simples - Relações entre classes
# Associação - usa, Agregação - tem
# Composição - É dono de, Herança - É um
#
# Herança vs Composição
#
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, child class, derived class

class Pessoa:
    cpf = '155234'
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
        
    def fala_nome_class(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)
        
class Cliente(Pessoa):
    def fala_nome_class(self):
        print('Eita, Nem sair da class CLIENTE')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno(Pessoa):
    cpf = 'CPF Aluno'

c1 = Cliente('Caio', 'Dias')
a1 = Aluno('Vini', 'Mendz')
c1.fala_nome_class()
a1.fala_nome_class()

print(a1.cpf)

# help(Aluno)
# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes.

# string = 'Caio'
# print(string.upper())
# print(isinstance(string, str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
p1 = Pessoa('Caio', 'Dias')
# p1.nome = 'Caio'
# p1.sobrenome = 'Dias'

p2 = Pessoa('Vini', 'Mendz')
# p2.nome = 'Vini'
# p2.sobrenome = 'Mendez'

print('P1:')
print(p1.nome)
print(p1.sobrenome)

print()

print('P2:')
print(p2.nome)
print(p2.sobrenome)
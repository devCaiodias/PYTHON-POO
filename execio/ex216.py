# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None
        
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, nome):
        self._motor = nome
        
    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, nome):
        self._fabricante = nome
        
        
        
class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante: 
    def __init__(self, nome):
        self.nome = nome

ferrari = Carro('Ferrari')
careira = Motor('9400 careira')
ford = Fabricante('Ford')
ferrari.motor = careira
ferrari.fabricante = ford

maquilaria = Carro('Maquilaria')
toyta = Fabricante('Toyta')
maquilaria.motor = careira
maquilaria.fabricante = toyta

print(ferrari.nome)
print(ferrari.motor.nome)
print(ferrari.fabricante.nome)
print()
print(maquilaria.nome)
print(maquilaria.motor.nome)
print(maquilaria.fabricante.nome)
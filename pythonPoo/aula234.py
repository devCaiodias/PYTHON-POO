# __new__ e __init__ em classes Python
# __new__ é o método responsável por criar e
# retornar o novo objeto. Por isso, new recebe cls.
# __new__ ❗️DEVE retornar o novo objeto❗️
# __init__ é o método responsável por inicializar
# a instância. Por isso, init recebe self.
# __init__ ❗️NÃO DEVE retornar nada (None)❗️
# object é a super classe de uma classe
class A:
    def __new__(cls, *args, **kwargs):
        # print('Criar coisa antes, de criar a intancia')
        intancia = super().__new__(cls)
        # print('Depois')
        # intancia.x = 2566
        return intancia
        
    def __init__(self, x):
        self.x = x
        print('sou o init')
        
    def __repr__(self):
        return 'A()'
    
a = A(156)
print(a.x)
# a = object.__new__(A)
# a.__init__()
# print(a)
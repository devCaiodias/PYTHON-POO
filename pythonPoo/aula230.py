# abstractmethod para qualquer método já decorado (@property e setter)
# É possível criar @property @property.setter @classmethod
# @staticmethod e métodos normais como abstratos, para isso
# use @abstractmethod como decorator mais interno.
# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação.
from abc import ABC, abstractmethod


class AbstractFoo(ABC):
    def __init__(self, nome):
        self._nome = None
        self.nome = nome
        
    @property
    # @abstractmethod
    def nome(self): 
        return self._nome
    
    @nome.setter
    @abstractmethod
    def nome(self, valor):
        self._nome = valor
        
        
class Foo(AbstractFoo):
    
    def __init__(self, nome):
        super().__init__(nome)
        # print('Sou inutil')
        
    # @property
    # def nome(self): 
    #     return self._nome
       
    # @nome.setter
    # def nome(self, valor):
    #     self._nome = valor
        
    @AbstractFoo.nome.setter
    def nome(self, valor):
        self._nome = valor
    
    
        
        
foo = Foo('Bar')

print(foo.nome)
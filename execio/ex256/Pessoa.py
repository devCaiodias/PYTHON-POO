import conta

class Pessoa:
    def __init__(self, nome: str, idade: int) -> None:
        self.nome = nome
        self.idade = idade
        
    @property
    def pessoa_nome(self):
        return self._nome
    
    @pessoa_nome.setter
    def pessoa_nome(self, nome: str):
        self._nome = nome
    
    @property
    def pessoa_idade(self):
        return self._idade
    
    @pessoa_idade.setter
    def pessoa_idade(self, idade: int):
        self._idade = idade
        
class Cliente(Pessoa):
    pass
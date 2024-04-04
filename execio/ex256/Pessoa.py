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
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.nome!r}, {self.idade!r})'
        return f'{class_name}{attrs}'
        
class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int) -> None:
        super().__init__(nome, idade)
        self.conta: conta.Conta | None = None
        
if __name__ == '__main__':
    c1 = Cliente('Caio', 34)
    c1.conta = conta.ContaCorrente(1222,456,0,0)
    print(c1)
    print(c1.conta)
    
    c2 = Cliente('Vine', 24)
    c2.conta = conta.ContaPoupanca(3322,1122,0)
    print(c2)
    print(c2.conta)
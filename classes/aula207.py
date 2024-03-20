# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.
class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
     
    @classmethod
    def metado_class(cls):
        print('Hey')
        
    @classmethod
    def criar_com_50anos(cls, nome):
        return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônimo', idade)
        
p1 = Pessoa('Caio', 18)
p2 = Pessoa.criar_com_50anos('Geraldo')
p3 = Pessoa.criar_sem_nome(23)
print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
# print(Pessoa.ano)
# Pessoa.metado_class()
# random tem geradores de números pseudoaleatórios
# Obs.: números pseudoaleatórios significa que os números
# parecem ser aleatórios, mas na verdade não são. Portanto,
# este módulo não deve ser usado para segurança ou uso criptográfico.
# O motivo disso é que quando temos uma mesma entrada e um mesmo algorítimo,
# a saída pode ser previsível.
# doc: https://docs.python.org/pt-br/3/library/random.html
import random


# Funções:
# seed
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")

random.seed(0)

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(0, 10, 2)
print(r_range)

# random.randint(início, fim)
#   -> Gera um número inteiro aleatório dentro de um intervalo "sem passo"
r_range_int = random.randint(2, 20)
# print(r_range_int)

# random.uniform(início, fim)
#   -> Gera um número flutuante aleatório dentro de um intervalo "sem passo"
r_range_float = random.uniform(1.2, 10.9)
# print(r_range_float)

# random.shuffle(SequenciaMutável) -> Embaralha a lista original
nome = ['Caio', 'Debora', 'Vinicius', 'Joao']
# random.shuffle(nome)
# print(nome)

# random.sample(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (não repete)
# novos_nomes = random.sample(nome, k=2)
# print(novos_nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
novos_nomes = random.choices(nome, k=2)
# print(nome)
# print(novos_nomes)


# random.choice(Iterável) -> Escolhe um elemento do iterável
# print(random.choice(nome))

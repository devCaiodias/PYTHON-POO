# secrets gera números aleatórios seguros
import secrets
import string as s
from secrets import SystemRandom as Sr

print(''.join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=6)))

random = secrets.SystemRandom()


# print(secrets.randbelow(1000))
# print(secrets.choice([1, 10, 20]))


# Funções:
# seed
#   -> Inicializa o gerador de random (por isso "números pseudoaleatórios")

# N FAZ NADAAAA!!
random.seed(0)

# random.randrange(início, fim, passo)
#   -> Gera um número inteiro aleatório dentro de um intervalo específico
r_range = random.randrange(0, 10, 2)
# print(r_range)

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
novos_nomes = random.sample(nome, k=2)
# print(novos_nomes)

# random.choices(Iterável, k=N)
#   -> Escolhe elementos do iterável e retorna outro iterável (repete valores)
# novos_nomes = random.choices(nome, k=2)
# print(nome)
# print(novos_nomes)


# random.choice(Iterável) -> Escolhe um elemento do iterável
# print(random.choice(nome))



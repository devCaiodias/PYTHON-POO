# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)

class MeuError(Exception):
    pass

class OrError(Exception):
    pass

def levantar():
    exception_ = MeuError('My error')
    exception_.add_note('Olha a nota 1')
    exception_.add_note('vc errou isso ')
    raise exception_

try:
    levantar()
    
except (MeuError, ZeroDivisionError) as error:
    print(error.__class__.__name__)
    print(error)
    print()
    exception_ = OrError('Vou lança de novo')
    exception_.add_note('Mias uma nota')
    exception_.__notes__ += error.__notes__.copy()
    raise exception_ from error
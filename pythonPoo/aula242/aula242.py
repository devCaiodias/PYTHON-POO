# Context Manager com função - Criando e Usando gerenciadores de contexto
from contextlib import contextmanager

@contextmanager
def my_open(caminho_file, modo):
    try:
        print('Open file')
        file = open(caminho_file, modo, encoding='utf8')
        yield file
    except Exception as e:
        print('O correu erro', e)
    finally:
        print('closing file')
        file.close()
    

with my_open('C:\\Users\\caiod\\pythonPOO\\pythonPoo\\aula242\\aula242.txt', 'w') as file:
    file.write('Caio \n')
    file.write('Vini \n',153)
    file.write('Debora \n')
    print('WITH', file)
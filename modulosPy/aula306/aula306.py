# sys.argv - Executando arquivos com argumentos no sistema
# Fonte = Fira Code
import sys

argumentos = sys.argv

qtd_argumentos = len(argumentos)

if qtd_argumentos <= 1:
    print('Vc n passou nem um argumento')
else:
    try:
        print(f'Vc passou {argumentos[1:]} argumentos')
        print(f'Vc passou {argumentos[1]} argumentos')
        print(f'Vc passou {argumentos[2]} argumentos')
    except IndexError:
        print('Falta argumentos. São 2 argumentos')
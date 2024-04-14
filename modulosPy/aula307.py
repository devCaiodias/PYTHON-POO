# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo" na tela.', 
    # type= str, #Tipo do argumento
    metavar='STRING',
    # default='Olá mundo', #Valor padrão
    required=False,
    action='append', #Recebe o argumento mais de um vez 
    # nargs='+', # Recebe mais de um valor 
    )

parser.add_argument(
    '-v', '--verbose',
    help='Mostra "Mostre logs',
    action='store_true'
    )
args = parser.parse_args()

if args.basic is None:
    print('Vc n passou valor de B')
    print(args.basic)
else:
    print('Valor de Basic: ', args.basic)
    
print(args.verbose)
# string.Template para substituir variáveis em textos
# doc: https://docs.python.org/3/library/string.html#template-strings
# Métodos:
# substitute: substitui mas gera erros se faltar chaves
# safe_substitute: substitui sem gerar erros
# Você também pode trocar o delimitador e outras coisas criando uma subclasse
# de template.

import string
import locale 
from datetime import datetime
import json

locale.setlocale(locale.LC_ALL, '')

def converter_para_brl(numero:float | int) -> str:
    blr = 'R$' + locale.currency(val=numero, symbol=False, grouping=True)
    return blr

data = datetime(2022, 12, 28)
dados = dict(
    nome='Caio', 
    valor= converter_para_brl(1_238_169),
    data= data.strftime('%d/%m/%Y'),
    empresa='C. Y', 
    telefone='+55 (66) 1111-2222'
)

# print(json.dumps(dados, indent= 2, ensure_ascii=False))

# texto = '''
# Prezado $nome

# Imformamos que sua mensalidade será cobrada no valor de $valor no dia $data. Caso
# deseja cancelar o serviço, entre em contato com a $empresa pelo telefone $telefone.

# Atenciosamente, 

# ${empresa}, 
# Abraço
# '''

CAMINHO_TXT = 'C:\\Users\\caiod\\pythonPOO\\modulosPy\\aula298\\aula298.txt'

with open(CAMINHO_TXT, 'r', encoding='utf8') as file:
    texto = file.read()
    template = string.Template(texto)
    print(template.substitute(dados))

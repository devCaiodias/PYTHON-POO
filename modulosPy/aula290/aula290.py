# json.dump e json.load com arquivos
import json
import os

NOME_ARQUIVO = 'C:\\Users\\caiod\\pythonPOO\\modulosPy\\aula290\\aula290.json'
CAMINHO_ABSOLUTO_ARQUIVO = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        NOME_ARQUIVO
    )
)

print(os.path.dirname(__file__))

filme = {
    'title': 'O Senhor dos Anéis: A Sociedade do Anel',
    'original_title': 'The Lord of the Rings: The Fellowship of the Ring',

    'is_movie': True,
    'imdb_rating': 8.8,
    'year': 2001,
    'characters': ['Frodo', 'Sam', 'Gandalf', 'Legolas', 'Boromir'],
    'budget': None
}

with open(CAMINHO_ABSOLUTO_ARQUIVO, 'w', encoding='utf8') as  file:
    json.dump(filme, file, ensure_ascii=False, indent= 2)


with open(CAMINHO_ABSOLUTO_ARQUIVO, 'r', encoding='utf8') as file:
    fime_do_json = json.load(file)
    print(fime_do_json)
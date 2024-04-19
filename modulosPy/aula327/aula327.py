# # PyPDF2 para manipular arquivos PDF (Instalação)
# PyPDF2 é uma biblioteca de manipulação de arquivos PDF feita em Python puro,
# gratuita e de código aberto. Ela é capaz de ler, manipular, escrever e unir
# dados de arquivos PDF, assim como adicionar anotações, transformar páginas,
# extrair texto e imagens, manipular metadados, e mais.
# A documentação contém todas as informações necessárias para usar PyPDF2.
# Link: https://pypdf2.readthedocs.io/en/3.0.0/
# Ative seu ambiente virtual
# pip install pypdf2
from pathlib import Path
import PyPDF2

CAMINHO_PASTA = Path(__file__).parent
CAMINHO_PDF = CAMINHO_PASTA / 'pdf'
CAMINHOS_NOVOS = CAMINHO_PASTA / 'arquivos_novos'

RELATORIO_BACEN = CAMINHO_PDF / 'R20230210.pdf'

CAMINHOS_NOVOS.mkdir(exist_ok=True)

reader = PyPDF2.PdfReader(RELATORIO_BACEN)

# print(len(reader.pages))
# for page in reader.pages:
#     print(page)
#     print()

page0 = reader.pages[0]
imagem0 = page0.images[0]

# print(page0.extract_text())
# with open(CAMINHOS_NOVOS / imagem0.name, 'wb') as imagem:
#     imagem.write(imagem0.data)
    

# writer.add_page(page0)



for i, page in enumerate(reader.pages):
    writer = PyPDF2.PdfWriter()
    with open(CAMINHOS_NOVOS / f'pages{i}.pdf', 'wb') as pdf:
            writer.add_page(page)
            writer.write(pdf)
            
merger = PyPDF2.PdfMerger()

files = [ 
    CAMINHOS_NOVOS / 'pages1.pdf',
    CAMINHOS_NOVOS / 'pages0.pdf',
    
         ]

for file in files:
    merger.append(file)
    
merger.write(CAMINHOS_NOVOS / 'MERGER.pdf')
merger.close()
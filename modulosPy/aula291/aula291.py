from pathlib import Path

caminho_projeto = Path()

# print(caminho_projeto.absolute()) 

caminho_file = Path(__file__)
# print(caminho_file)

ideia = caminho_file.parent / 'ideias'
# print(ideia / 'file.txt')

caminho_file = Path.home() / 'Desktop' / 'file.txt'

caminho_file.touch()
# print(file)
caminho_file.write_text('Olá mundo!!!!')
# print(file.read_text())
caminho_file.unlink()
# caminho_file.write_text('')
# with open(caminho_file, 'a+') as file:
#     file.write('1 LINHA \n')
#     file.write('2 LINHA \n')
    
# print(caminho_file.read_text())

caminho_pasta = Path.home() / 'Desktop' / 'Python é legal'
caminho_pasta.mkdir(exist_ok=True)

subpasta = caminho_pasta / 'subpasta'
subpasta.mkdir(exist_ok=True)

outro_file = subpasta / 'file.txt'
outro_file.touch()
outro_file.write_text('subpasta')
# print(outro_file.read_text())

mais_file = caminho_pasta / 'file.txt'
mais_file.touch()
mais_file.write_text('caminho pasta')

# caminho_pasta.rmdir()

files = caminho_pasta / 'files'
files.mkdir(exist_ok=True)

for i in range(10):
    file = files / f'file_{i}.txt'
    
    if file.exists():
        file.unlink()
    else:
        file.touch()
        
    with open(file, 'a+') as file:
        file.write('Ola mundo\n')
        file.write(f'file_{i}.txt')
        
def rmtree(root: Path, remove_root=True):
    for file in root.glob('*'):
        if file.is_dir():
            print('Dir: ', file)
            rmtree(file, False)
            file.rmdir()
        else:
            print('file: ', file)
            file.unlink()
    
    if remove_root:
        root.rmdir()
    
rmtree(caminho_pasta)
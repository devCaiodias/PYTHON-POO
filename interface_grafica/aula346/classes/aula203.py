# Mantendo estados dentro da classe
class Camera:
    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
        
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} já está filmando...')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True
        
    def parar_de_filmar(self):
        if not self.filmando:
            print(f'{self.nome} N está filmando...')
            return
        
        print(f'{self.nome} está parando de filmar')
        self.filmando = False
        
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} N pode fotografar filmando...')
            return
        
        print(f'{self.nome} está fotografando....')
 
print('C1:')       
c1 = Camera('juju')
print(c1.nome)

c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_de_filmar()
c1.fotografar()

# print(c1.filmando)




print()

print('C2:')
c2 = Camera('papo')
print(c2.nome)

c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_de_filmar()
c2.fotografar()
c2.parar_de_filmar()
# Método especial __call__
# callable é algo que pode ser executado com parênteses
# Em classes normais, __call__ faz a instância de uma
# classe "callable".


class CallMe:
    def __init__(self, phone):
        self.phone = phone
        
    def __call__(self, nome):
        print(nome, 'Chamando o', self.phone)
        return 2156
        
call1 = CallMe('14886654')
retorno = call1('Caio Dias')
print(retorno)

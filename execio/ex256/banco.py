import conta
import Pessoa

class Banco:
    def __init__(
        self,
        agencias: list[int] | None = None,
        clientes: list[Pessoa.Pessoa] | None = None,
        contas: list[ conta.Conta] | None = None
                 ):
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
        
        # self.cliente: Pessoa.Cliente | None = None
        # self.conta: conta.Conta | None = None
        
    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False
      
    def _checa_cliente(self, cliente):
        if cliente in self.clientes:
            return True
        return False  
     
    def _checa_contas(self, conta):
        if conta in self.contas:
            return True
        return False 
    
    def autenticar(self, cliente, conta):
        if conta.agencia in self.agencias:
            return True
        return False
    
    # def __repr__(self):
    #     class_name = type(self).__name__
    #     attrs = f'({self.cliente!r}, {self.conta!r})'
    #     return f'{class_name}{attrs}'
        
        
if __name__ == '__main__':
    b1 = Banco()
    # b1.cliente = Pessoa.Cliente('Caio', 15)
    # b1.conta = conta.ContaCorrente(2211,3322, 0 , 0)
    
    print(b1)
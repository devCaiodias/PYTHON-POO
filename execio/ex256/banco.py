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
    
    def _checa_se_conta_e_do_cliente(self, cliente, conta):
        if conta is cliente.conta:
            return True
        return False
    
    def autenticar(self, cliente: Pessoa.Cliente, conta: conta.Conta):
        return self._checa_agencia(conta) and \
            self._checa_cliente(cliente) and \
                self._checa_contas(conta) and \
                    self._checa_se_conta_e_do_cliente(cliente, conta)
                
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencias!r}, {self.clientes!r}, {self.contas!r})'
        return f'{class_name}{attrs}'
        
        
if __name__ == '__main__':
    c1 = Pessoa.Cliente('Caio', 34)
    c_Corrente1 = conta.ContaCorrente(1222,456,0,0)
    c1.conta = c_Corrente1
    
    c2 = Pessoa.Cliente('Vine', 24)
    c_Poupanca2 = conta.ContaPoupanca(3322,1122,0)
    c2.conta = c_Poupanca2
    
    
    banco = Banco()
    banco.clientes.extend([c1,c2])
    banco.contas.extend([c_Corrente1, c_Poupanca2])
    banco.agencias.extend([1222,3322])
    
    if banco.autenticar(c1, c_Corrente1):
        c_Corrente1.depositar(100)
        c_Corrente1.sacar(98)
from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia: int, conta: int, saldo: float =0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    @abstractmethod
    def sacar(self, valor: float) -> float:
        pass
        
    def depositar(self, valor: float):
        self.saldo += valor  
        self.detalhes(f'(Depositar {valor})')  
    
    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f}, {msg}')
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, '\
        f' {self.saldo!r})'
        return f'{class_name}{attrs}'
        
        
class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        
        if valor_pos_saque > 0:
            self.saldo -= valor
            self.detalhes(f'(Sacar {valor})')
            return self.saldo
        else:
            print('N foi possivel sacar o valor desejado')
            self.detalhes(f'(Saque Negado {valor})')
            return self.saldo
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, '\
            f'{self.saldo!r})'
        return f'{class_name}{attrs}'
        
class ContaCorrente(Conta):
    def __init__(self, agencia: int, conta: int, saldo: float =0 , limite: float =0):
        super().__init__(agencia,conta, saldo)
        self.limite = limite
        
    def sacar(self, valor: float) -> float:
        valor_pos_saque = self.saldo - valor
        limite_maximo = -self.limite
        
        if valor_pos_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'(Sacar {valor})')
            return self.saldo
        else:
            print('N foi possivel sacar o valor desejado')
            print(f'Seu limite é , {-self.limite:.2f}')
            self.detalhes(f'(Saque Negado {valor})')
            return self.saldo
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'({self.agencia!r}, {self.conta!r}, '\
            f'{self.saldo!r}, {self.limite!r})'
        return f'{class_name}{attrs}'
        
if __name__ == '__main__':
    c_Poupanca = ContaPoupanca(2564,4758)
    c_Poupanca.sacar(1)
    c_Poupanca.depositar(1)
    c_Poupanca.sacar(1)
    c_Poupanca.sacar(1)
    print('##')
    c_Corrente =  ContaCorrente(2564,4758, 0, 100)
    c_Corrente.sacar(1)
    c_Corrente.depositar(1)
    c_Corrente.sacar(1)
    c_Corrente.sacar(1)
    c_Corrente.sacar(98)
    c_Corrente.sacar(1)
    
    
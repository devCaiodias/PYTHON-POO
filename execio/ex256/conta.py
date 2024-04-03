from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    @abstractmethod
    def sacar(self, valor):
        pass
        
    def depositar(self, valor):
        self.saldo += valor  
        self.detalhes(f'Depositar {valor}')  
    
    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo:.2f}, {msg}')
        
        
class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_pos_saque = self.saldo - valor
        
        if valor_pos_saque > 0:
            self.saldo -= valor
            self.detalhes(f'Sacar {valor}')
        else:
            print('N foi possivel sacar o valor desejado')
            self.detalhes(f'Saque Negado {valor}')
        
        
if __name__ == '__main__':
    c_Poupanca = ContaPoupanca(2564,4758,0)
    c_Poupanca.depositar(20)
    c_Poupanca.sacar(2)
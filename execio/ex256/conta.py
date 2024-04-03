from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
    
    @abstractmethod
    def sacar(self, valor):
        self.saldo - valor
        self.detalhes('Sacar')
        
    def depositar(self, valor):
        self.saldo += valor  
        self.detalhes(f'Depositar {valor}')  
    
    def detalhes(self, msg=''):
        print(f'O seu saldo é {self.saldo}, {msg}')
        
        
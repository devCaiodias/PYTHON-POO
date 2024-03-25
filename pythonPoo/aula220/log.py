# Abstração
class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o métado log')
    
    def log_erro(self,msg):
        return self._log(f'Erro: {msg}')
                 
    def log_sucesso(self,msg):
        return self._log(f'Sucesso: {msg}')
    
class LogFileMixin(Log):
    def _log(self, msg):
        print(msg)
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')
    
    

# Testa programa 
if __name__ == '__main__':
    l = LogPrintMixin()
    l.log_erro('Vixiii')
    l.log_sucesso('Caio')
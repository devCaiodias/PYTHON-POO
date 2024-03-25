# Abstração
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'
class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o métado log')
    
    def log_erro(self,msg):
        return self._log(f'Erro: {msg}')
                 
    def log_sucesso(self,msg):
        return self._log(f'Sucesso: {msg}')
    
class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print('SALVANDO...', {msg_formatada})
        with open(LOG_FILE, 'a', encoding='utf8') as file:
            file.write(msg_formatada)
            file.write('\n')
    
class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')
    
    

# Testa programa 
if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_erro('Vixiii')
    lp.log_sucesso('Caio')
    lf = LogFileMixin()
    lf.log_erro('Vixiii')
    lf.log_sucesso('Caio')
# Abstração
class Log:
    def log(self, msg):
        raise NotImplementedError('Implemente o métado log')
    
class LogFileMixin(Log):
    def log(self, msg):
        print(msg)
    
    

# Testa programa 
if __name__ == '__main__':    
    l = LogFileMixin()
    l.log('Caio')
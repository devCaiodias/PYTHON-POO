# Funções decoradoras e decoradores com classes

def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name} ({class_dict})'
        return class_repr

def adicionar_repr(cls):
    # def meu_repr(self):
    #     class_name = self.__class__.__name__
    #     class_dict = self.__dict__
    #     class_repr = f'{class_name} ({class_dict})'
    #     return class_repr
    cls.__repr__ = meu_repr
    return cls        

# class ReprMixin:
#     def __repr__(self):
#         class_name = self.__class__.__name__
#         class_dict = self.__dict__
#         class_repr = f'{class_name} ({class_dict})'
#         return class_repr

@adicionar_repr
class Time:
    def __init__(self, nome):
        self.nome = nome
        
        
@adicionar_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome
        
# Time = adicionar_repr(Time)

brasil = Time('Brasil')
portugal = Time('Portugal')

# Planeta = adicionar_repr(Planeta)

terra = Planeta('Terra')
marte = Planeta('Marte')


print(brasil)
print(portugal)
print(terra)
print(marte)
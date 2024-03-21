# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       não DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi
#       declarado.
class Foo:
    def __init__(self):
        self.public = 'Isso é publico'
        self._protected = 'Isso é protected'
        self.__private = 'Isso é private'
        
    def metado_public(self):
        # self._metado_protected()
        # print(self._protected)
        print(self.__private)
        self.__metado_private()
        return 'metado_public'
    
    def _metado_protected(self):
        print('_metado_protected')
        return '_metado_protected'
    
    def __metado_private(self):
        print('__metado_private')
        return '__metado_private'
        
f1 = Foo()
# print(f1.public)
print(f1.metado_public())
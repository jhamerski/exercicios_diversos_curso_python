"""
POO - HERANÇA MÚLTIPLA

Nada mais é do que a possibilidade de uma classe herdar de múltiplas classes, fazendo com que a classe filha herde todos
os atributos e métodos das classes herdadas

OBS: A herança múltipla pode ser feita de duas maneiras:
    - Multiderivação direta.
    - Multiderivação indireta.

Não importa se a derivação é direta ou indireta. A Classe que realiza-rá a herança herdará todos os atributos e métodos
da super classe

# Multiderivação direta
class Base1:
    pass


class Base2:
    pass


class Multiderivada(Base1, Base2):
    pass


# Multiderivação Indireta
class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class Multiderivada(Base3):
    pass
"""


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def nadar(self):
        return f'O {self._Animal__nome} está nadando....'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} do mar!'


class Terrestre(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def andar(self):
        return f'O {self._Animal__nome} está andando...'

    def cumprimentar(self):
        return f'Eu sou {self._Animal__nome} da terra!'


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome):
        super().__init__(nome)


# Testando
baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())

teta = Pinguim('Teta')
print(teta.nadar())
print(teta.andar())
print(teta.cumprimentar())  # Method Resolution Order - MRO

# Objeto instância de ...
print(f'Teta é instância de Pinguim? {isinstance(teta, Pinguim)}')
print(f'Teta é instância de Aquático? {isinstance(teta, Aquatico)}')
print(f'Teta é instância de Terrestre? {isinstance(teta, Terrestre)}')
print(f'Teta é instância de Animal? {isinstance(teta, Animal)}')
print(f'Teta é instância de object? {isinstance(teta, object)}')

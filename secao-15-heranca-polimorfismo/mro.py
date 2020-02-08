"""
POO - METHOD RESOLUTION ORDER


É a ordem de execução dos métodos, em Python, podemos conferir a ordem de execução dos métodos de 3 formas:
    - Via propriedade da classe __mro__
    - Via método mro()
    - Via hel
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


class Pinguim(Aquatico, Terrestre):

    def __init__(self, nome):
        super().__init__(nome)


teta = Pinguim('Teta')
print(teta.cumprimentar())  # Method Resolution Order - MRO

print(Pinguim.__mro__)
#  (<class '__main__.Pinguim'>, <class '__main__.Aquatico'>, <class '__main__.Terrestre'>, <class '__main__.Animal'>, <class 'object'>)
print(Pinguim.mro())
print(help(Pinguim))
"""
class Pinguim(Terrestre, Aquatico):
Eu sou Teta da terra!

class Pinguim(Aquatico, Terrestre):
Eu sou Teta do mar!
"""


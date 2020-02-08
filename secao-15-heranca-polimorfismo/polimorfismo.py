"""
POO - POLIMORFISMO

Objetos que podem se comportar de forma diferente

Quando implementamos um método presente na classe pai em classes filhas estamos realizando uma sobrescrita de método
chamada (Overriding)

O Overriding é a melhor representação do Polimorfismo
"""


class Animal(object):

    def __init__(self, nome):
        self.__nome = nome

    def falar(self):
        raise NotImplementedError('A classe filha precisa implementar esse método')

    def comer(self):
        print(f'{self.__nome} está comendo...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} faz au-au')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} faz miau')


class Rato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def falar(self):
        print(f'{self._Animal__nome} fala algo')


dog = Cachorro('Bilu')
dog.falar()
dog.comer()

cat = Gato('Felix')
cat.falar()
cat.comer()

rat = Rato('Stuart')
rat.falar()
rat.comer()

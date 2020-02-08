"""
CONHECENDO O PICKLE

A função Pickle realiza o seguinte processo:
Objeto Python -> Binarização
Binarização -> Objeto Python

Este processo é chamado de SEREALIZAÇÃO/DESEREALIZAÇÃO

OBS: O Módulo pickle() não é seguro contra dados maliciosos e dessa forma não é recomendado trabalhar com arquivos
pickle vindo de outras pessoas que você não conheça ou de fontes desconhecidas.
"""
import pickle


class Animal:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        print(f'{self.__nome} está comendo')


class Gato(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def mia(self):
        print(f'{self.nome} está miando...')


class Cachorro(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def late(self):
        print(f'{self.nome} está latindo...')


felix = Gato('Felix')
pluto = Cachorro('Pluto')

with open('animais.pickle', 'wb') as arq:
    pickle.dump((felix, pluto), arq)

# Como fazer a leitura de dados em arquivos pickle
with open('Animais.pickle', 'rb') as arq:
    gato, cachorro = pickle.load(arq)
    print(f'O gato chama-se {gato.nome}')
    gato.mia()
    print(f'O tipo do gato é {type(gato)}')

    print(f'O cachorro chama-se {cachorro.nome}')
    cachorro.late()
    print(f'O tipo de cachorro é {type(cachorro)}')

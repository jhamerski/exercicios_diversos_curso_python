"""
POO - MÉTODO SUPER

O método super() se refere a super classe
"""


class Animal:

    def __init__(self, nome, especie):
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        print(f'O {self.__nome} faz {som}')


class Gato(Animal):

    def __init__(self, nome, especie, raca):
        super().__init__(nome, especie)
        # Animal.__initi(self, nome, especie, raca)
        super().faz_som('Grrrr')
        self.__raca = raca


felix = Gato('Felix', 'Felino', 'Angorá')
felix.faz_som('Miau-Miau')


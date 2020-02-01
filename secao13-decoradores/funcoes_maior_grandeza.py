"""
FUNÇÕES DE MAIOR GRANDEZA - Higher Order Functons - HOF

O que isso significa?
- Quando uma linguagem de programação suporta HOF, indica que podemos ter funções que retornam outras funções como
resultado, ou mesmo que podemos passar funções como argumentos para outras funções, ou até mesmo criar variáveis do tipo
de funções nos nossos programas.

OBS: Na seção de funções nós utilizamos isso

Em Python, as funções são Cidadões de Primeira Classe, First Class Citizen
"""


# Exemplo - Definindo as funções
def somar(a, b):
    return a + b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)


# Testando as funções
print(calcular(4, 3, somar))
print(calcular(4, 3, diminuir))
print(calcular(4, 3, multiplicar))
print(calcular(4, 3, dividir))

# Nested Function - Funções aninhadas
"""
Podemos ter funções dentro de funções que são conhecidas por Nested Functions ou também Inner Functions que são 
(funções Internas)
"""
from random import choice


def cumprimento(pessoa):
    def humor():
        return choice(('E aí ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa


print(cumprimento('Jonas'))


# Retornando funções de outras funções
def faz_me_rir():
    def rir():
        return choice(('hahahaha', 'kkkkkkk', 'rsrsrsrs'))
    return rir


rindo = faz_me_rir()

print(rindo())

# Inner Functions / Nested Funcitons podem acessar o escopo de funções mais externas


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(('hahaha', 'kkkkkk', 'rsrsrs'))
        return f'{risada} {pessoa}'
    return dando_risada


rindo = faz_me_rir_novamente('Jonas')

print(rindo())
print(rindo())
print(rindo())

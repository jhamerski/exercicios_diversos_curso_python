"""
MÓDULO RANDOM

random() -> Possui várias funções para números pseudo-aleatório.

OBS: Módulos nada mais são do que outros arquivos PYTHON.

- Ao realizar o import todo o módulo, todas as funções, atributos, classes e propriedades  que estiverem dentro do
módulo ficarão em memória (disponível). Caso saiba quais funções precisa utilizar, importe somente elas.

help(random.random) documentação do que a função faz.

Não confunda a função random() com o pacote random, pode parecer confuso, mas a função random() é apenas uma função
dentro do módulo random.

Existem duas formas de se utilizar um módulo ou função deste
Foma 1 - Importando todo o módulo (Não recomendado).
import random

dir(random) -> lista todas as funções e propriedades que ele tem
print(random.random())  # random() -> gera um número real pseudo-aleatório entre 0 e 1. Para utilizar a função, precisamos
colocar o nome do pacote e o nome da função, separados por ponto(.)

# Importando uma função específica do módulo
from random import random  # Nesse importe, estamos falando: do módulo random importe a função random()
for i in range(10):
    print(random())
"""
# uniform() -> Gerar um número real pseudo-aleatório entre os valores estabelecidos
from random import uniform
for i in range(10):
    print(uniform(3, 7))  # 7 não é incluído

# randint() -> Gera valores pseudo-aleatórios entre os valores estabelecidos
from random import randint
for i in range(6):
    print(randint(1, 61))

# choice() -> Mostra um valor aleatório entre um iterável
from random import choice
jogadas = ['pedra', 'papel', 'tesoura']
print(choice(jogadas))
print(choice('Jonas Hamerski'))

# suffle() -> Tem a função de embaralhar dados
from random import shuffle
cartas = ['A', "K", 'Q', 'J', '2', '3', '4', '5', '6']
print(cartas)
shuffle(cartas)
print(cartas[0])

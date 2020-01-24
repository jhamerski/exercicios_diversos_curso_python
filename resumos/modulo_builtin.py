"""
MÓDULO BUILT-IN (Integrados, ou seja, já vem instalados no Python)

Link dos módulos integrados: https://docs.python.org/3/py-modindex.html

"""
# Utilizando alias (apelidos) para módulos e funções
import random as rdm
print(rdm.random())

# Podemos utilizar todas as funções de um módulo utilizando o *
from random import *
print(random())

# Importando todo o módulo
import random
print(random.random())

# Utilizando alias (apelidos) para módulos e funções
from random import randint as rdi, random as rdm
print(rdi(5, 89))
print(rdm())

# Costumamos utilizar tuple para colocar vários imports do mesmo módulo
from random import (
    random,
    randint,
    shuffle,
    choice
)
print(random())
print(randint(1, 11))
lista = [1, 2, 3, 4, 5]
shuffle(lista)
print(lista)
print(choice('Hamerski'))


"""
DICTIONARY COMPREHENSION

Criar lista
lista = [1, 2, 3, 4]
[valor for valor in iterável]

Criar tupla
tupla = (1, 2, 3, 4) ou 1, 2, 3, 4,

Criar conjunto
conjunto = {1, 2, 3, 4}

Criar dicionário
dicionário = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

SINTAXE
{chave:valor for valor in iterável}
"""
from builtins import print

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)

numeros = [1, 2, 3, 4, 5]
quadrado_teste = {valor: valor ** 2 for valor in numeros}

print(quadrado_teste)

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]

mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}
print(mistura)

# Lógica condicional
nums = [1, 2, 3, 4, 5]
res = {num: ('par' if num % 2 == 0 else 'ímpar') for num in nums}
print(res)

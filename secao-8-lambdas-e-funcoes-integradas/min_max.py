"""
MIN e MAX

max() -> Retorna o maior valor de um iterável ou o maior de dois ou mais elementos.
Faça um programa que receba dois números do usuário e retorne o maior número deles
val1 = int(input('Informe o 1° valor: '))
val2 = int(input('Informe o 2° valor: '))
print(max(val1, val2))


min() -> Retorna o menor valor de um iterável ou o menor de dois ou mais elementos.
"""
lista = [1, 8, 4, 34, 99, 129]
print(max(lista))

tupla = (1, 8, 4, 34, 99, 129)
print(max(tupla))

conjunto = {1, 8, 4, 34, 99, 129}
print(max(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 34, 'e': 99, 'f': 129}
print(max(dicionario))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 34, 'e': 99, 'f': 129}
print(max(dicionario.values()))  # Valores do dicionário

print(max(3, 34))

print(max('a', 'b', 'abc'))

print(max('a', 'b', 'c', 'j'))

print(30 * '-=')

lista = [1, 8, 4, 34, 99, 129]
print(min(lista))

tupla = (1, 8, 4, 34, 99, 129)
print(min(tupla))

conjunto = {1, 8, 4, 34, 99, 129}
print(min(conjunto))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 34, 'e': 99, 'f': 129}
print(min(dicionario))

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 34, 'e': 99, 'f': 129}
print(min(dicionario.values()))  # Valores do dicionário

print(max(3, 34))

print(min('a', 'b', 'abc'))

print(min('a', 'b', 'c', 'j'))

# Outros exmplos
nomes = ['Jonas', 'Julia', 'Carlos', 'Francielle', 'Marcos', 'Tim']
print(max(nomes))  # M arcos
print(min(nomes))  # C arlos

print(max(nomes, key=lambda nome: len(nome)))  # Francielle
print(min(nomes, key=lambda nome: len(nome)))  # Tim

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Master', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 4},
    {'titulo': 'Too old to rock in roll, too young to die', 'tocou': 32}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print(min(musicas, key=lambda musica: musica['tocou']))

# DESAFIO! Imprima somente o título da música mais e menos tocada?
print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])  # Acrescentei a chave
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])  # Acrescentei a chave

# DESAFIO! Como encontrar a música mais tocada e menos tocada sem usar, max(), min(), lambda?
max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

min = 99999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])
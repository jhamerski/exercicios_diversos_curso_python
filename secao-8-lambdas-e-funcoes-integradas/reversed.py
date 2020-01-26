"""
REVERSED

OBS: Não confunda com a função reverse() que estudamos nas listas. A função reverse() só funciona em listas.
Já a função REVERSED() funciona com qualquer iterável.

A função reversed() retorna um iterável chamado List Reverse Iterator

"""
# reverse()
lista = [1, 2, 3, 4, 5]
lista.reverse()
print(lista)

lista = [1, 2, 3, 4, 5]
res = reversed(lista)
print(res)
print(type(res))

# Podemos converter o elemento retornado para listas, tuplas e conjuntos
print(list(reversed(lista)))
print(tuple(reversed(lista)))
print(set(reversed(lista)))  # Ordem dos elementos não definidas

# Iterando
for letra in reversed('Jonas Hamerski'):
    print(letra, end='')

print('\n')
# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed('Jonas Hamerski'))))

# slice de String
print('Jonas Hamerski' [::-1])

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n, end='')

print('\n')
# Podemos utilizar o próprio range
for n in range(9, -1, -1):
    print(n, end='-')

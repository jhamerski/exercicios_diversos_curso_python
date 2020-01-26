"""
ANY and ALL

Funções integradas: Aquelas que não precisam de importação

all() -> Retorna True se todos os elementos do iterável são verdadeiros ou ainda se o iterável está vazio.
any() -> Retorna True se qualquer elemento do iterável for verdadeiro. Se o iterável estiver vazio, retorna FALSE.
"""
# Exemplo all()
print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros? - False por causa do 0
print(all([1, 2, 3, 4]))  # Todos os números são verdadeiros? - True
print(all([]))  # Lista vazia? - True
print(all((1, 2, 3, 4)))  # Todos os números são verdadeiros? - True
print(all({1, 2, 3, 4}))  # Todos os números são verdadeiros? - True
print(all('Jonas Hamerski'))  # Todos os números são verdadeiros? - True

nomes = ['Carlos', 'Camila', 'Cassiano', 'Caio', 'Daniel']
print(all([nome[0] == 'C' for nome in nomes]))
nomes = ['Carlos', 'Camila', 'Cassiano', 'Caio']
print(all([nome[0] == 'C' for nome in nomes]))

# OBS: Um iterável vario em boolean é False, porém o all() considera como True
print(all([letra for letra in 'eio' if letra in 'aeiou']))

print(all(num for num in [4, 2, 6, 10, 8] if num % 2 == 0))
# OBS: Novamente gera uma lista vazia, continua sendo True
print(all(num for num in [4, 2, 6, 10, 8] if num % 2 != 0))
print(20 * '-=')

# any()
print('Abaixo exemplos de any()')
print(any([0, 1, 2, 3, 4]))  # True
print(all([0, False, (), {}, []]))  # False

nomes = ['Carlos', 'Camila', 'Cassiano', 'Caio', 'Daniel', 'Julia']

print(any([nome[0] == 'C' for nome in nomes]))

print(any([num for num in [2, 4, 6, 8, 9] if num % 2 == 0]))

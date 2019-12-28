"""
[LISTAS]

Listas são representadas por [colchetes]
Funcionam com vetores, matrizes (arrays), com a diferença de serem DINÂMICAS e podermos colocar QUALQUER tipo de dado

Em C ou Java:
- Array tem tamanho fixo e pode somente ter um tipo de dado.

PYHTON:
- Dinâmico: Não possui tamanho fixo, ou seja, podemos criar a lista e ir adicionando elementos.
"""
type([])

lista1 = [1, 3, 5, 7, 9, 2, 4, 6, 8]

lista2 = ['J', 'o', 'n', 'a', 's']

lista3 = []

lista4 = list(range(11))

lista5 = list('Jonas Hamerski')

# Podemos checar se determinado valor está contido na lista
if 8 in lista4:
    print('Encontrei o número 8.')

# Podemos ordenar a lista
lista1.sort()
print(lista1)

# Podemos contar as ocorrências de um determinado valor
print(lista5.count('a'))

# Adicionar elementos, utilizamos a funcao append() 'acescentar' OBS: Apenas um elemento por cada vez
# ERRADO lista5.append('1', '2', '3')
lista5.append('!')
print(lista5)

# extend() coloca cada elemento como valor adicional
lista5.extend('Francielle Barreto')
print(lista5)

lista1.extend([10, 11, 12, 13])
print(lista1)

# Adicionando informando o índice usando o insert()
lista1.insert(0, 'Valor Zero')
print(lista1)

# Juntar listas
lista6 = lista1 + lista2
print(lista6)

# Lista inversa usando reverse()
lista2.reverse()
print(lista2)

# Copiar uma lista
lista7 = lista2.copy()
print(lista7)

# Tamanho de uma lista
print(len(lista5))

# Remover e retornar o último elemento pop()
lista2.pop()
print(lista2)

# Remover pelo indice pop(1)
lista2.pop(2)
print(lista2)

# Remover todos clear()
lista2.clear()
print(lista2)

# Repetir elementos
lista1 = lista1 * 3
print(lista1)

# Transformando String em uma lista split()
curso = 'Jonas Hamerski está aprendendo Python'
print(curso)
curso = curso.split()
print(curso)



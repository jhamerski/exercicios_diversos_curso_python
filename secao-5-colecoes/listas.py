"""
[LISTAS] - list

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

# Adicionar elementos, utilizamos a funcao append() 'acrescentar' OBS: Apenas um elemento por cada vez
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

# Convertendo uma lista em String
lista8 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista8)
conversao = ' '.join(lista8)  # Colocando espaço e transformando em uma lista
print(conversao)

conversao = '$'.join(lista8)  # Colocando $ em cada espaço da lista
print(conversao)

# Vários elementos dentro de uma lista, inclusive outra lista
lista9 = [1, 1.5, True, 'Jonas', 'H', (1, 2, 3), 32423424]
print(lista9)
print(type(lista9))

# ITERANDO SOBRE LISTAS
for elemento in lista9:
    print(elemento)

carrinho = []
produtos = ''
while produtos != 'sair':
    produtos = input('Informe o produto: ')
    if produtos != 'sair':
        carrinho.append(produtos)

for produtos in carrinho:
    print(produtos)

# Utilizando variáveis em listas
num1 = 1
num2 = 2
num3 = 3

lista10 = [num1, num2, num3]
print(lista10)

# Fazemos acesso aos elementos de forma indexada
#           0         1           2
cores = ['verde', 'amarelo', 'vermelho']
print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # vermelho
# Podemos acessar de forma inversa (pense na lista como um círculo)
print(cores[-1])  # vermelho
print(cores[-2])  # amarelo

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):  # cores = 3
    print(cores[indice])
    indice += 1

# Buscando um indíce
for indice, cor in enumerate(cores):
    print(indice, cor)


# Aceitam valores repetidos
lista11 = []
lista11.append(42)
lista11.append(42)
lista11.append(6)
lista11.append(8)
print(lista11)

# Outros métodos úteis
# Encontrar indíces de outras forma. Se não tiver o elemento, vai ocorrer VALUE ERROR
numeros = [5, 5, 6, 7, 8, 5, 9]
print(numeros.index(6))
print(numeros.index(9))
print(numeros.index(5))  # retorna o índice do primeiro elemento encontrado
print(numeros.index(5, 3))  # encontrar o elemento (5) a partir do índice 3
print(numeros.index(7, 2, 4))  # encontrar o elemento (7) entre o índice 2 e 4

# Revisão slicing() lista[início:fim:passo] ou range(início:fim:passo)
lista12 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(lista12[1:])  # iniciando no índice 1
print(lista12[3:6])  # iniciando no índice 3 e terminando no 6
print(lista12[:13:2])  # iniciando no índice 0, terminando no índice 13 com intervalo de 2 em 2

# Invertendo valores
nomes = ['Jonas', 'Hamerski']
print(nomes)
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)
nomes.reverse()
print(nomes)

# Soma*, valor Máximo*, valor Mínimo* e tamanho (*Todos valores inteiros ou reais)
lista13 = [1, 2, 3, 4, 5, 6]
print(sum(lista13))
print(max(lista13))
print(min(lista13))
print(len(lista13))

print(type(lista13))
tupla = tuple(lista13)
print(type(tupla))

# Desenpacotamento de listas. OBS: O número de elementos precisa ser o MESMO do número de variáveis, senão VALUE ERROR
lista14 = [1, 2, 3]
num1, num2, num3 = lista14
print(num1)
print(num2)
print(num3)

# Copiando lista (Deep Copy or Shallow Copy)
lista15 = [1, 2, 3]
print(lista15)

nova = lista15.copy()  # Cópia profunda, não afeta a lista original
print(nova)
nova.append(4)
print(lista15)
print(nova)

lista16 = [1, 2, 3]  # Cópia rasa, as duas listas são alteradas
print(lista16)
nova = lista16
print(nova)
nova.append(4)
print(nova)
print(lista16)

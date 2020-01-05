"""
LISTAS ANINHADAS (NESTED LISTS)

Algumas linguagens de programação (C, JAVA, PHP) possuem uma estrutura de dados chamados arrays:
    - Unidimensionais (Arrays, Vetores)
    - Multidimensionais (Matrizes)

Em Python nós temos as listas

listas = [1, True, 1.34, 'ok']
"""
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # 3X3
print(listas)
print(type(listas))

# Acessando os dados
print(listas[0][1])  # Acessando a primeira lista o segundo elemento (índice 1, valor 2)
print(listas[2][1])  # 8

# Iterando com loops em listas aninhadas
for lista in listas:
    print(lista)

for lista in listas:
    for num in lista:
        print(num, end=" ")
    print()

# List comprehension
[[print(valor) for valor in lista] for lista in listas]

# Gerando uma matriz 3X3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

velha = [['X' if numero % 2 == 0 else 'O' for numero in range(1, 4)] for valor in range(1, 4)]
print(velha)

# Gerando valores iniciais
print([["*" for i in range(1, 4)] for j in range(1, 4)])

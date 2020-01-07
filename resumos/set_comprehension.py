"""
SET COMPREHENSION

lita = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}
"""
numeros = {num for num in range(1, 7)}
print(numeros)

numeros = {x ** 2 for x in range(10)}
print(numeros)

# Tranformando a estrutura acima em um dicionário
numeros = {x: x ** 2 for x in range(10)}
print(numeros)

# String
letras = {letra for letra in 'Jonas Hamerski'}  # Valores não se repetem, também não tem ordenação
print(letras)

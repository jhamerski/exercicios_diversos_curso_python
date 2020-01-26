"""
LIST COMPREHENSION

- Utilizando o list comprehension, nós podemos gerar novas listas com dados processados a partir de outro iterável
SINTAXE:
[ dado for dado in iterável ]

Para entender melhor, devemos dividir a expressão em duas partes:
- Primeira parte: for numero in numeros
- Segunda parte: numero * 10
"""
numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]
print(res)

outra = [numero / 2 for numero in numeros]
print(outra)


def funcao(valor):
    return valor * valor


teste = [funcao(numero) for numero in numeros]
print(teste)

# List comprehension VS loop
# loop
numeros_dobrados = []
for numero in [1, 2, 3, 4, 5]:
    numeros_dobrados.append(numero * 2)

print(numeros_dobrados)

# list comprehension
print([numeros * 2 for numeros in numeros])

nome = 'Jonas Hamerski'
print([letra.upper() for letra in nome])


def caixa_alta(nome):
    nome = nome.replace(nome[0], nome[0].upper())
    return nome


amigos = ['Carlos', 'Julia', 'Paulo', 'Nicolas']
print([caixa_alta(amigo) for amigo in amigos])

print([numero * 3 for numero in range(1, 10)])

print([bool(valor) for valor in [0, [], (), True, 3.14, 1.68]])

print([str(numeros) for numeros in [1, 2, 3, 4, 5]])

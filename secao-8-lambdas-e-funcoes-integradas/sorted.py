"""
SORTED

Não confunda, apenar do nome, com a função sort() que já estudamos em listas. O sort() só funciona em listas

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio no diz, sorted() serve para ordenar

OBS: o sorted() SEMPRE retorna uma lista com os elementos do iterável ordenados
"""
# Relembrando sort()
lista = [4, 3, 1, 1, 5, 2, 6]
lista.sort()
print(lista)

# Utilizando o sorted

numeros = (1, 5, 3, 2)
print(numeros)
print(sorted(numeros))  # Ordena do menor para o maior
print(numeros)

# Adicionando parâmetros
num = [1, 5, 3, 2]
print(sorted(num))
print(sorted(num, reverse=True))  # Ordena do MAIOR para o menor

# Converter para um set()
print(set(sorted(num)))

# Utilizando com mais complexidade
usuarios = [
    {'username': 'jonas', 'tweets': ['Eu adoro bolos', 'Eu adoro pizzas']},
    {'username': 'carlos', 'tweets': ['Eu amo gatos']},
    {'username': 'julia', 'tweets': []},
    {'username': 'francielle', 'tweets': [], 'cor': 'amarelo'},
    {'username': 'arthur', 'tweets': ['Eu gosto de carne', 'Vou sair hoje']},
    {'username': 'paulo', 'tweets': [], 'cor': 'preto', 'musica': 'rock'},
]
print(usuarios)

# Ordenando pelo username
print(sorted(usuarios, key=lambda usuario: usuario['username']))

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))

musicas = [
    {'titulo': 'Thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Master', 'tocou': 2},
    {'titulo': 'Back in Black', 'tocou': 4},
    {'titulo': 'Too old to rock in roll, too young to die', 'tocou': 32}
]

# Ordem crescente
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordem decrescente
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))

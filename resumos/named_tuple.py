"""
NAMED TUPLE

São tuplas diferenciadas, ondem específicamos um nome para a mesma e também parâmetros.
"""
from collections import namedtuple
tupla = (11, 32, 53)
print(tupla[1])

# Declaração
cachorro = namedtuple('cachorro', 'idade raca nome')

cachorro = namedtuple('cachorro', 'idade, raca, nome')

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando
ray = cachorro(idade=2, raca='Chow-Chow', nome='ray')
print(ray)

# Acessando os dados
print(ray[0])  # idade
print(ray[1])  # raca
print(ray[2])  # nome

print(ray.idade)  # idade
print(ray.raca)  # raca
print(ray.nome)  # nome

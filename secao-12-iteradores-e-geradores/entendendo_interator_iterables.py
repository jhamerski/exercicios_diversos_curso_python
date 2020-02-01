"""
ENTENDENDO ITERATORS E ITERABLES

Iterator:
    - Um objeto que pode ser iterado
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma função next() é chamada

Iterable:
    - Um objeto que irá retornar um iterator quando a função iter() for chamada.

lista = [1, 2, 3, 4, 5]  # Iterable mas náo é um interator

# print(next(nome))  # TypeError: 'str' object is not an iterator

it1 = iter(nome)
it2 = iter(lista)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
"""
nome = 'Jonas'  # Iterable mas náo é um interator

for letra in nome:
    print(letra)

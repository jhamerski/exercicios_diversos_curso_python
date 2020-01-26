"""
GENERATORS EXPRESSION

Estudamos anteriormente:
- Lista Comprehension
- Dictionary Comprehension
- Set Comprehension

Não vimos as tuples comprehension... porque elas se chama Generators

"""
from sys import getsizeof

# List Comprehension
nomes = ['Carlos', 'Caio', 'Camila', 'Vanessa']
print(any([nome[0] == 'C' for nome in nomes]))
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

# Generator
print(any(nome[0] == 'C' for nome in nomes))
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

# getsizeof() -> retorna a quantidade de bytes do elemento passado como parâmetro
print(getsizeof('Jonas'))  # mostra quantos bytes a string Jonas está ocupando em memória
print(getsizeof('Hamersk'))
print(getsizeof(9))
print(getsizeof(2342342342))
print(getsizeof(True))

# Gerando uma lista de números com list compreheison
list_comp = getsizeof([x * 10 for x in range(1000)])

# Gerando uma lista de números com set compreheison
set_comp = getsizeof({x * 10 for x in range(1000)})

# Gerando uma lista de números com dictionary compreheison
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

# Gerando uma lista de número com generator
gen = getsizeof(x * 10 for x in range(1000))

print(30 * "-=")
print('Para fazer a mesma tarefa gastamos em memória!')
print(f'List Comprehension: {list_comp} bytes.')
print(f'Set Comprehension: {set_comp} bytes.')
print(f'Dictionary Comprehension: {dic_comp} bytes.')
print(f'Generator Expression: {gen} bytes.')

gen = (x * 10 for x in range(1000))
print(type(gen))
print(gen)

for num in gen:
    print(num)

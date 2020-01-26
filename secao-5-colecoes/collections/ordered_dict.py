"""
ORDERED DICT

É um dicionário que nos garante a ordenação conforme inserção
"""
from collections import OrderedDict

# A ordem de inserção não é garantida
dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
print(dicionario)

for chave, valor in dicionario.items():
    print(f'Chave={chave} : Valor={valor}')

# Aqui garantimos a ordenação conforme inserção
dicionario_dois = OrderedDict({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
for chave, valor in dicionario_dois.items():
    print(f'Chave={chave} : Valor={valor}')

# Dicionários comuns
dict_one = {'a': 1, 'b': 2}
dict_two = {'b': 2, 'a': 1}
print(dict_one == dict_two)  # True, já que a ordem dos elementos não importa para o dicionário

# Ordered Dict
odict_one = OrderedDict({'a': 1, 'b': 2})
odict_two = OrderedDict({'b': 2, 'a': 1})
print(odict_one == odict_two)  # False, pois a ordem dos elementos importam

"""
MAPAS

Conhecidos em python como dicionários

Dicionários em Python são representadas por {chaves}

"""
receita = {'jan': 100, 'fev': 250, 'mar': 310}

# Iterar nos dicionários
for chave in receita:
    print(chave)

for valores in receita:
    print(receita[valores])

for chave in receita:
    print(f'Em {chave} recebi ${receita[chave]}')

# Acessando as chaves
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

# Acessando os valores
print(receita.values())

for valores in receita.values():
    print(valores)

# Desempacotamento de dicionários

print(receita.items())

for chave, valor in receita.items():
    print(f'Chave:{chave} - Valor:{valor}')

# Soma*, valor máximo*, valor mínimo*, tamanho   *Os valores devem ser todos int ou float
print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

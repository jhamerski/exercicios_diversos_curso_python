"""
STRING

Tudo que tiver entre aspas simples, duplas ou triplas
"""
name = 'Jonas \nHamerski'
print(name)

name_um = """Francielle
Barreto"""
print(name_um.upper())

# Colocando o texto em uma lista (dividida)
print(name.split())

# Imprime da posição 0 até a 4
print(name_um[0:4])

# Transforma em lista e acesso o segundo elemento "dividida"
# ['Francielle', 'Barreto']
# [       0    ,     1    ]
print(name_um.split()[1])

# Comece do primeiro elemento, vai até o último e inverta
print(name_um[::-1])

# Substituindo 'a' por 'A' "substituir"
print(name_um.replace('a', 'A'))

texto = 'socorram me subino onibus em marrocos'
print(texto[::-1])

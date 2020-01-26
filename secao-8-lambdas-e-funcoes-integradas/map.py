"""
MAP

Com map fazemps mapeamento de valores para função. Ela recebe dois parâmetros, o 1° é a função e o 2° o iterável

Para fixar:
- Temos dados iteráveis:
    - dados: a1, a2, ... an
- Temos uma função:
    - f(x)

Utilizamos a função map(f(x), dados) onde o map irá mapear cada elemento dos dados e aplicar a função. O <map object>
é feito o retorno da seguinte forma: f(a1), f(a2), ..., f(an)
"""
import math


def area(r):
    """Calcula a área de um circulo com Raio 'r'."""
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))

raios = [2, 5, 7.1, 0.3, 10, 44]
# Forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

# Forma com map
areas = map(area, raios)  # Recebendo dois parâmetros: 1° função e 2° iterrável
print(areas)
print(type(areas))
print(list(areas))

# Map com lambda
print('Map com lambda')
print(list(map(lambda r: math.pi * (r ** 2), raios)))
# OBS: Após utilizar a primeira vez a função map, ele zera o resultado

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28)]
print(cidades)

# Transforma para f = 9/5 * c + 32
c_para_f = lambda dado: (dado[0], (9/5 * dado[1] + 32))

print(list(map(c_para_f, cidades)))

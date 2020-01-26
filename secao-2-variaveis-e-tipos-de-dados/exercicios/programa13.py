"""
Esvreva um programa que leia as coordenas X e Y de pontos R² e calcule sua distância da origem (0, 0)
"""
import math

x = float(input('Informe um ponto X: '))

y = float(input('Informe um ponto Y: '))

distancia = math.sqrt(x ** 2 + y ** 2)

print(f'A distancia entre os pontos {x} e {y} é: {distancia}')

"""
Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pinta-la. Sabendo que para cada litro de tinta, pinta uma área de 2m²
"""
alt = float(input('Informe o altura da parede: '))
lar = float(input('Informe a largura da parede: '))
total = alt * lar
print(f'Sua parede tem as dimensões de {alt}x{lar} e sua área é de {total}m².')
litros = total / 2
print(f'Para pintar essa parede, você precisa de {litros}l de tinta.')

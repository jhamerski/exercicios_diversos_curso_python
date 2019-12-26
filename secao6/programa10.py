"""
Faça um programa que calcule e mostre a soma dos 50 primeiros números pares
"""
soma = 0

for num in range(1, 101):
    if num % 2 == 0:
        soma = soma + num
print(f'A soma dos 50 primeiros números pares foi de: {soma}')

"""
Faça um programa que leia um número inteiro e positivo. Gere outro número formado pelos dígitos invertidos
do mesmo número.
"""
number = int(input('Informe um número inteiro e positivo: '))

while number > 1:
    inverter = int(number % 10)
    number /= int(10)
    print(inverter, end='')

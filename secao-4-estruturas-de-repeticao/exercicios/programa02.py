"""
Faça um programa que escreva na tela, de 1 até 100, de 1 em 1, 2 vezes. A primeira deve usar o for e a segunda o while
"""
for numero in range(1, 101):
    print(numero, end='-')
print()

num = 1
while num <= 100:
    print(num, end='-')
    num = num + 1

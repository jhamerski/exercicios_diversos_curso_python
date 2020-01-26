"""
Crie um programa que lê 6 números inteiros, em seguida, mostre na tela os valores lidos.
"""
lista = []

for i in range(1, 7):
    lista.append(int(input(f'Informe o {i} numero: ')))

print('-=' * 30)
print(f'Segue lista: {lista}')

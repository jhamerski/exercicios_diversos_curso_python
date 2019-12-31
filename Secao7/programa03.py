"""
Faça um programa que receba um vetor de 10 posições, em seguida deverá ser impresso o maior e o menor elemento do vetor
"""
vetor = []

for i in range(1, 11):
    vetor.append(float(input(f'Informe o {i}° elemento: ')))

print(f'O maior número digitado foi: {max(vetor)}. O menor número digitado foi: {min(vetor)}')

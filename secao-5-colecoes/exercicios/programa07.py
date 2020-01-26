"""
Leia um vetor de 10 números reais, ordene os elementos deste vetor, e no final escreva o vetor ordenado.
"""
vetor = []

for i in range(10):
    vetor.append(float(input(f'Escreve o elemento {i + 1}: ')))

print(f'Vetor original: {vetor}')

print(f'O vetor ordenado é {sorted(vetor)}')

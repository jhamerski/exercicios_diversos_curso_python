"""
Faça uma função que receba um vetor de inteiros e retorne o maior valor.
"""
qtd = int(input('Informe a quantidade de elemento que deseja inseir no vetor: '))


def add_elementos(tamanho):
    vetor = []
    for i in range(1, tamanho + 1):
        vetor.append(int(input(f'Informe o {i}° número: ')))

    print(max(vetor))  # Opção Pythonica

    maior = 0
    for i in range(1, len(vetor)):
        if i == 1:
            maior = vetor[0]
        if maior < vetor[i]:
            maior = vetor[i]

    print(f'O maior número digitado no vetor foi: {maior}')
    return vetor


print(add_elementos(qtd))

"""
Faça um programa que receba do usuário um arquivo texto e mostre na tela quantos linhas esse arquivo possui
"""
caminho = input('Informe o caminho do seu arquivo .txt: ')

with open(f'{caminho}') as arquivo:
    print(len(arquivo.readlines()))

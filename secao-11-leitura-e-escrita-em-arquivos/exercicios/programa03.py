"""
Faça um programa que receba de um usuário um arquivo e mostre na tela quantas letras são vogais
"""
caminho = input('Informe o caminho de um arquivo texto: ')

with open(f'{caminho}') as arquivo:
    contador = 0
    vogais = 'aeiou'
    arquivo = "".join(arquivo)
    for letra in arquivo:
        print(letra, end='')
        if letra.lower() in vogais:
            contador += 1

print(f'\nO arquivo {caminho} tem {contador} letras vogais.')

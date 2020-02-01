"""
Faça um programa que receba do usuário um arquivo texto. Crie outro texto contendo o texto do arquivo de entrada, mas com
as vogais substituídas por '*'
"""
caminho = input('Informe o caminho do arquivo: ')

with open(f'{caminho}') as arq:
    vogais = 'aeiou'
    arq = ''.join(arq)
    for letra in arq:
        with open('resultado.txt', 'a') as res:
            if letra.lower() in vogais:
                res.write('*')
            else:
                res.write(letra)

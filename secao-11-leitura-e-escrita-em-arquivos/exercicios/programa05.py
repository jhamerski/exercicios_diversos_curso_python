"""
Faça um programa que leia o conteúdo de um arquivo e crie um arquivo com o mesmo conteúdo, mas com todas as letras
minúsculas convertidas para maíusculas. Os nomes dos arquivos serão fornecidos, via teclado, pelo usuário.
"""
caminho = input('Informe o caminho do arquivo: ')

arq_res = input('Informe o nome do arquivo resultante: ')

with open(f'{caminho}') as arq:
    with open(f'{arq_res}.txt', 'a') as res:
        res.write(arq.read().upper())

print(f'Foi gerado o arquivo: {arq_res}.txt')

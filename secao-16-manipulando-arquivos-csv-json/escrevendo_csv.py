"""
ESCREVENDO ARQUIVOS .CSV

reader() -> Leitor  writer() -> Escritor

from csv import writer, DictWriter

with open('filmes.csv', 'a') as arq:
    escritor_csv = writer(arq)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])  # Método para escrever cada linha, recebe uma lista
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input(f'Informe o gnero do {filme}: ')
            duracao = input(f'Informe a duração em (minutos) do {filme}: ')
            escritor_csv.writerow([filme, genero, duracao])
"""
# DictWriter
from csv import DictWriter

# As chaves do dicionário, devem ser as mesmas utilizadas no cabecalho

with open('filmes_outros.csv', 'a') as arq:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escrever = DictWriter(arq, fieldnames=cabecalho)
    escrever.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o filme: ')
        if filme != 'sair':
            genero = input(f'Informe o gênero do {filme}: ')
            duracao = input(f'Informe a duração em (minutos) do {filme}: ')
            escrever.writerow({'Título': filme, 'Gênero': genero, 'Duração': duracao})


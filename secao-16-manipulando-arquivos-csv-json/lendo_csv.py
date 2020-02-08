"""
LENDO ARQUIVOS .CSV

CSV -> Comma Separeted Values (Valores Separados por Vírgula)
Por vírgula:
    1, 2, 3, 4, 5
    "jonas", "hamerski", "06-02-2020"

Por ponto e vírgula
    1; 2; 3; 4; 5
    "jonas"; "hamerski"; "06-02-2020"

Por espaço
    1 2 3 4 5
    "jonas" "hamerski" "06-02-2020"

OBS: Podemos ter qualquer separador, desde que tenha um padrão

Python possui duas formas diferentes para ler dados de arquivos .csv
    - reader -> Permite que iteremos sobre as linhas do arquivo CSV como listas
    - DictReader -> Permite que iteremos sobre as linhas como OrderedDicts
"""
# Forma possível, mas não é a ideal
with open('lutadores.csv', encoding='utf-8') as arq:
    dados = arq.read()
    # print(type(dados))
    dados = dados.split(',')[2:]
    print(dados)

print('')
from csv import reader

with open('lutadores.csv', encoding='utf-8') as arq:
    leitor_csv = reader(arq)
    next(leitor_csv)  # Pular o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu no(a) {linha[1]} e mede {linha[2]}cm.')

print('')
from csv import DictReader

with open('lutadores.csv', encoding='utf-8') as arq:
    leitura = DictReader(arq)
    for linha in leitura:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}cm.")

print('')
# Com outro delimitador
with open('lutadores.csv', encoding='utf-8') as arq:
    leitura = DictReader(arq, delimiter=',')
    for linha in leitura:
        # Cada linha é um OrderedDict
        print(f"{linha['Nome']} nasceu no(a) {linha['País']} e mede {linha['Altura (em cm)']}cm.")

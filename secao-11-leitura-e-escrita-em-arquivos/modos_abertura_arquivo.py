"""
MODOS ABERTURA DE ARQUIVO

r -> abre para leitura: padrão
w -> abre para escrita: sobrescreve caso o arquivo já exista
x -> abre para escrita somente se o arquivo não existir, caso ela exista, gera FileExistsError
a -> abre para a escrita, adicionando SEMPRE no final do arquivo caso ele já exista, caso não, será criado. OBS: Não
conseguimos controlar o cursor.
+ -> abre para o módulo de atualização: leitura e escrita
"""
# with open('test.txt', 'x') as arquivo:
#    arquivo.write('Teste de conteudo\n')

try:
    with open('test.txt', 'x') as arquivo:
        arquivo.write('Teste de conteudo\n')
except FileExistsError:
    print('Este arquivo já existe')

with open('nome_completo.txt', 'w') as nm:
    while True:
        nome = input('Informe seu nome completo ou digite sair: ')
        if nome != 'sair':
            nm.write(f'Seu nome completo é: {nome}\n')
        else:
            break


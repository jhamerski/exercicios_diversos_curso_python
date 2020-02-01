"""
ESCREVER EM ARQUIVOS

OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele, apenas ler. Da mesma forma, se abrirmos um
arquivo para a escrita, não podemos ler, apenas escrever.

Ao abrir um arquivo para a escrita, o mesmo é criado no sistema operacional.

OBS: Devemos sempre passar uma String como parâmetros na função write(), senão gera TypeError

Abrindo o arquivo em modo 'w', se o arquivo não existir, ele será criado, caso ele já exista, o anterior será apagado e
o novo será criado, ou seja, todo o conteúdo anterior será perdido.
"""
# Escrevendo em arquivo . 'w' write (escrita)
with open('novo.txt', 'w') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil. \nPodemos colocar quantas linhas quisermos.\n Com novos'
                  'dados')

# Gerando um arquivo com dados do usuário
with open('nome_completo.txt', 'w') as nm:
    while True:
        nome = input('Informe seu nome completo ou digite "sair": ')
        if nome != 'sair':
            nm.write(f'Seu nome completo é: {nome}\n')
        else:
            break
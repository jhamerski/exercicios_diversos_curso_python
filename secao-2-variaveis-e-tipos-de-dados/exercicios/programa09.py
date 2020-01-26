"""
Faça um programa para ler as dimnesões de um terreno (comprimento c e largura l), bem como o preço do metro de tela p.
Imprima o custo para cercar este mesmo terreno com tela
"""
comprimento = float(input('Informe o comprimento do terreno: '))
largura = float(input('Informe a largura do terreno: '))
preco = float(input('Informe o preço do metro da tela: R$'))

total = (comprimento * 2 + largura * 2) * preco

print(f'O valor total referente a tela, para cercar o terreno é de {total}')

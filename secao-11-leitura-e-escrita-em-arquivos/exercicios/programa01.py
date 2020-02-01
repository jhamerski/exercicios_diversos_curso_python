"""
Escreva um programa que:
a) Crie um arquivo texto de nome "arq.txt"
b) Permita que o usuário grave diversos caracteres nesse arquivo, até que o usuário entre com o carctér '0'
c) Feche o arquivo
Agora abra e leia o arquivo, caracter por carcter, e escreva na tela todos os caracteres armazenados
"""
with open('arq.txt', 'a') as arquivo:
    while True:
        caracter = input('Digite algo e "0" para sair: ')
        if caracter != '0':
            arquivo.write(f'{caracter}\n')
        else:
            break

with open('arq.txt') as result:
    result = "".join(result)
    for letra in result:
        print(letra)

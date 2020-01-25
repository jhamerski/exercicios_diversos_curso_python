"""
LOOP - WHILE

While (expressao_booleana):
    //execução do loop
Será repetido enquanto a opção for verdadeira
"""
numero = 1
while numero <= 10:
    print(f'{numero} - ', end='')
    numero = numero + 1
print()

resposta = ' '
while resposta != 'sim':
    resposta = input('Já terminou...')

"""
Escreva um MENU de opções. Leia a opção do usuário e execute a operação escolhida. Escreva uma mensagem de ERRO se a
opção for inválida
Escolha a opção:
1- Soma de 2 números
2- Diferença entre 2 números
3- Produto entre 2 números
4- Divisão entre dois números (denominador não pode ser 0 (zero))
"""
print('---------------MENU---------------')
print('1- Soma de 2 números.')
print('2- Diferença entre 2 números.')
print('3- Produto entre 2 números.')
print('4- Divisão entre dois números.')

opcao = int(input('Escolha a operação que deseja fazer: '))

if opcao == 1:
    num_um = float(input('Primeiro Número: '))
    num_dois = float(input('Segundo Número: '))
    result = num_um + num_dois
    print(f'A soma de {num_um} + {num_dois} é: {result}')
elif opcao == 2:
    num_um = float(input('Primeiro Número: '))
    num_dois = float(input('Segundo Número: '))
    result = num_um - num_dois
    print(f'A diferença de {num_um} - {num_dois} é: {result}')
elif opcao == 3:
    num_um = float(input('Primeiro Número: '))
    num_dois = float(input('Segundo Número: '))
    result = num_um * num_dois
    print(f'O produto de {num_um} * {num_dois} é: {result}')
elif opcao == 4:
    num_um = float(input('Primeiro Número: '))
    num_dois = float(input('Segundo Número: '))
    if num_dois == 0:
        print('Denominador 0 (zero). Impossível fazer a divisão!')
    result = num_um / num_dois
    print(f'A divisão de {num_um} / {num_dois} é: {result}')
else:
    print('Opção inválida. ERRO!')


"""
Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido prorporcionalmente ao valor que cada deu
na realização da a aposta. Faça um programa que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto
cada um ganharia do prêmio com base no valor investido
"""
premio = float(input('Informe o valor do prêmio: R$'))
jogador_um = float(input('Jogador 01 - Informe o valor que deseja apostar: '))
jogador_dois = float(input('Jogador 02 - Informe o valor que deseja apostar: '))
jogador_tres = float(input('Jogador 03 - Informe o valor que deseja apostar: '))

total_aposta = jogador_um + jogador_dois + jogador_tres

aux = float(premio / total_aposta)

recebe_um = aux * jogador_um
print(f'O Jogador 01 apostou {jogador_um} e recebe R${recebe_um}.')

recebe_dois = aux * jogador_dois
print(f'O Jogador 02 apostou {jogador_dois} e recebe R${recebe_dois}.')

recebe_tres = aux * jogador_tres
print(f'O Jogador 03 apostou {jogador_tres} e recebe R${recebe_tres}.')

"""
Leia um valor inteiro em segundos e imprima em horas, minutos e segundos
"""
seconds = int(input('Informe SEGUNDOS para transformar em HH:MM:ss -> '))

hours = int(seconds / 3600)
minutes = int((seconds - (hours * 3600)) / 60)
seconds = seconds % 60

print(f'{hours} : {minutes} : {seconds}')

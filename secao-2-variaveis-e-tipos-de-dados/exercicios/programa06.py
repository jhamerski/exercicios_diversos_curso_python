"""
Leia a temperatura em Graus Celsius e apresente-a convertida em Graus Fahrenheit. A fórmula do conversão é:
F = C * (9.0/5.0) + 32.0, sendo F(Fahrenheit) e C(Celsius)
"""
temp = float(input('Informe a temperatura em Grau Celsius: '))

far = temp * (9.0/5.0) + 32.0

print(f'{temp}° Graus Celsius equivalem a {far}° Graus Fahrenheit')

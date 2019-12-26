"""
Faça um programa para converter uma letra maíuscula em letra minúscula. Use a tabela ASCII para resolver o problema
"""
# Função ord() -> devolve o código numérico do caracter
letra = ord(input('Digite uma letra MAÍUSCULA: '))

letra += 32

# Função chr() -> devolve o caracter
print(chr(letra))


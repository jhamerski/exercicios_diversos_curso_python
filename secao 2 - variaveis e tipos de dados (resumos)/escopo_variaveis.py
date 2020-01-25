"""
ESCOPO

Globais: Compreende todo o programa
Locais: Reconhecidas apenas no bloco onde foram declaradas.

declarar_variavel_python = valor
E quando declaramos, não colocamos o tipo de dado dela, o tipo é inferido quando recebe o valor.
"""
x = 2  # variável global
if x > 10:
    novo = "Estou aqui"  # variável local

print(novo)

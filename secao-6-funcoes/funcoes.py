"""
FUNÇÔES

- São pequenos trechos de códigos que realizam tarefas específicas
- Podem ou não receber entrada de dados e retornar uma saída de dados
- Muito úteis para executar procedimentos similares, por repetidas vezes
-
OBS: Se escrever uma função que realiza várias tarefas dentro delas, é bom fazer uma verificação para que a função seja
simplificada
"""
# Utilização
cores = ['verde', 'amarelo', 'vermelho', 'branco']

# Utilizando função integrada (Buit-in) do Python
print(cores)

curso = 'Programação em Python'
print(curso)

cores.append('roxo')
print(cores)

# curso.append('Mais cursos') AttributeError
# DRY -> Don't Repeat YourSelf -> Não repita você mesmo / Não repita seu código

"""
Definir funções, em Python definimos por def nome_da_funcao(parametros_de_entrada):
    bloco da função

- Nome da função: sempre com letras minusculas, e se for nome composto, separado por underline(Snake Case)
- Parâmetros de entrada: são opcionais, onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não
- bloco da fução: Também chamado de corpo da função ou implementação, é onde o processo da função acontece, neste bloco
pode ter retorno ou não

OBS: Para definir uma função, utilizamos a palavra reservada 'def'  informando ao Python que estamos definindo uma 
função, também abrimos o bloco de código com o já conhecido : (dois pontos), que é utilizado em Python para definir 
blocos
"""
# Definindo a primeira função


def diz_oi():
    print('Oi')


"""
OBS: 
- Veja que dentro das nossas funções, podemos utilizar outras funções
- Nossa função só executa uma tarefa, ou seja, a única coisa que ela faz é dizer Oi
- Não recebe nenhum parâmetro de entrada
- Não retorna nada
"""

# Utilizando funções
diz_oi()  # Atenção: nunca esquece de utilizar o parenteses ao utilizar uma função


def cantar_parabens():
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Vida o aniversariante!')


cantar_parabens()
for i in range(2):
    print()
    cantar_parabens()

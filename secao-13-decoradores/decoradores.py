"""
DECORADORES (DECORATORS)

O que são Decorators?
    - São funções.
    - Envolvem outras funções e aprimoram seu comportamento.
    - Também são exemplos de Higher Order Functions
    - Tem uma sintaxe própria, usando '@' (Syntac Sugar / Açucar Sintático)

|-----------------------------------------------------------|
|               Funcation Decorator                         |
-------------------------------------------------------------

-------------------------------------------------------------
|  |---------------------------------------------------------|
|  |               Função Decorada (aprimora)                |
|  |---------------------------------------------------------|
|------------------------------------------------------------|

"""


# Decorator como funções (Sintaxe não recomendada/ sem açucar sintático)
def seja_educado(funcao):
    def sendo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um ótimo dia!')
    return sendo


def saudacao():
    print('Seja bem vindo(a) ao curso de Python')


# Testando 1
teste = seja_educado(saudacao)

# saudacao()

teste()


# Testando 2
def raiva():
    print('EU TE ODEIO!')


raiva_educada = seja_educado(raiva)

raiva_educada()


# Decorators com Syntax Sugar
def seja_educado_mesmo(funcao):
    def sendo_mesmo():
        print('Foi um prazer conhecer você!')
        funcao()
        print('Tenha um excelente dia!')
    return sendo_mesmo


@seja_educado_mesmo
def apresentando():
    print('Meu nome é Jonas.')


# Testando
apresentando()


@seja_educado_mesmo
def dormir():
    print('Quero dormir...')


dormir()

"""
|-------------------------------------------------------------|
|   HOME   |   Serviços   |   Produtos   |   Administrativo   |
|-------------------------------------------------------------|

Imagina que queira circular pelo menu, porém só a pessoa logada no site pode acessar a área administrativa

https://wwww.suaempresa.com.br/home
https://wwww.suaempresa.com.br/servicos
https://wwww.suaempresa.com.br/produtos
https://wwww.suaempresa.com.br/admin

OBS: Não é código funcional, é APENAS EXEMPLO
def checa_login():                                          --|
    if not request.usuario:                                    -| Decorator Function
        redirect('http://www.suaempresa.com.br/login')      --|


def home(request):
    return 'Pode acessar home.'
    
def servicos(request):
    return 'Pode acessar serviços.'
    
def produtos(request):
    return 'Pode acessar produtos.'

@checa_login  -> DECORATOR
def admin(request):
    return 'Pode acessar admin.'
    
OBS: Não confunda Decorator com Decorator Function
"""

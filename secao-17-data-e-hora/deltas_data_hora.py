"""
TRABALHANDO COM DELTAS DE DATA E HORA

É a diferença entre uma e outra
result = data_final - data_inicial


"""
import datetime

# Data de hoje
data_hoje = datetime.datetime.now()

# Data futura que ocorre um evento
niver = datetime.datetime(2020, 3, 24)

# Calculando o delta
print(f'Faltam {(niver - data_hoje).days} dias para seu aniversário!')

# Adicionando dias em um boleto
data_compra = datetime.datetime.now()

print(data_compra)

regra_boleto = datetime.timedelta(days=3)

print(regra_boleto)

vencimento_compra = data_compra + regra_boleto

print(f'Sua compra foi feita hoje: {data_compra.day}/{data_compra.month}')
print(f'Seu boleto vence dia: {vencimento_compra.day}/{vencimento_compra.month}')

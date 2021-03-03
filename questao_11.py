'''
11) Altere o programa anterior de forma a perguntar também o valor depositado mensalmente.
    Esse valor será depositado no início de cada mês, e você deve considerá-lo para o cálculo
    de juros do mês seguinte.

'''

deposito_inicial = float(input('Informe um valor do deposito inicial: '))
taxa_juros = float(input('Informe a taxa de juros: '))

meses = 12
ganho_mesal = 0
ganho_total = 0

for mes in range(1, meses + 1):
    deposito = float(input('Informe o valor que deseja depositar no mes %d :' %mes))
    deposito_inicial += deposito
    ganho_mesal = (taxa_juros / 100) * deposito_inicial
    ganho_total += ganho_mesal
    deposito_inicial += ganho_mesal
    print(f'O valor da conta no mes {mes} eh {deposito_inicial:.2f} R$')

print(f'O valor total que foi ganho com os juros foi de {ganho_total:.2f} R$')






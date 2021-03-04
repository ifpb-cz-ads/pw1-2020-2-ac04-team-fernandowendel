# Questao 12

divida = float(input("Informe o valor da Divida: R$ "))
taxa = float(input("Informe a taxa de juros: "))
pagamento = float(input("Informe o valor da parcela: R$ "))

mes = 1

if (divida * (taxa/100) >= pagamento):
    print("Sua dívida não será paga nunca, parcela menor que a taxa de juros.")
else:
    saldo = divida
    juros_pago = 0
    while saldo > pagamento:
        juros = saldo * taxa / 100
        saldo = saldo + juros - pagamento
        juros_pago = juros_pago + juros
        print ("Saldo da dívida no mês %d é de R$%6.2f." % (mes, saldo))
        mes = mes + 1
    print ("você precisará de %d meses, pagando um total de R$%.2f de juros." % (mes-1, juros_pago))
    print ("Total pago com juros: R$%.2f " % (divida+juros_pago))
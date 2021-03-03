# Questao 10

deposito = float(input("Informe o valor do deposito: R$ "))
taxa = float(input("Informe o percentua de juros: "))

cont = 1
soma = deposito
ganho = 0

while cont <= 12:
    soma = soma + (soma * taxa / 100)
    print("Mes %.d R$ %.2f" % (cont, soma))
    cont+=1
ganho = soma - deposito
print("Ganho em juros de R$ %.2f ao final de 12 meses." % ganho)
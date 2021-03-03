# Questao 14

pagar = 0
while True:
    cod = int(input("Código da mercadoria (0 para sair):"))
    preco = 0
    if cod == 0:
        break;
    elif cod == 1:
        preco = 0.50
    elif cod == 2:
        preco = 1.00
    elif cod == 3:
        preco = 4.00
    elif cod == 5:
        preco = 7.00
    elif cod == 9:
        preco = 8.00
    else:
        print("Código inválido!")
    if preco != 0:
        quantidade = int(input("Informe a quantidade: "))
        pagar = pagar + (preco * quantidade)
print("Total a pagar: R$%.2f" % pagar)
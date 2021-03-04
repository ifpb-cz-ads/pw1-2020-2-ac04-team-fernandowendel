# Questao 08

n1 = int(input("Informe um numero: "))
n2 = int(input("Informe outro numero: "))

cont = 0
resto = n1

while resto != 0:
    resto = resto - n2
    cont+=1
print("%.d / %.d = %.d e tem resto = %.d" % (n1, n2, cont, resto))
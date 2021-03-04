# Questao 18

dividendo = int(input("Informe o dividendo: "))
divisor = int(input("Informe o divisor: "))
quociente = 0
x = dividendo
while x >= divisor:
    x = x - divisor
    quociente = quociente + 1
resto = x
print("O resto da divisao de %d / %d é %d" % (dividendo,divisor,resto))
'''
3) Modifique o programa abaixo para imprimir de 1 até o número digitado pelo usuário,
   mas, dessa vez, apenas os números ímpares.

    fim = int(input("Digite o último número a imprimir:"))
    x = 0
    while x <= fim:
        print(x)
        x = x + 2


'''

fim = int(input('Digite o último número a imprimir: '))
x = 1

while x <= fim:
    
    if x == fim or x % 2 != 0:
        print(x)

    x += 1
'''
17) Modifique o programa anterior de forma a ler um número n. 
    Imprima os n primeiros números primos.

'''

n = int(input('Informe um numero: '))
contador = 0
numero = 1

while contador < n:

    numero += 1
    verificar = True
    x = 2

    while x < numero:
        if numero % x == 0:

            verificar = False

        if x == 2:

            x += 1

        else: 
            
            x += 2

    if verificar:
        contador += 1
        print(f'{numero}')
        



   
    





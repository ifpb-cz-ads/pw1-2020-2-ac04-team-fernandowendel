'''
15) Escreva um programa que exiba uma lista de opções (menu): 
    adição, subtração, divisão, multiplicação e sair. 
    Imprima a tabuada da operação escolhida. Repita até que a opção "saída" seja escolhida.

'''

while True:
    print('\n1 --> Imprimir a tabuada de adicao')
    print('2 --> Imprimir a tabuada de Subtracao')
    print('3 --> Imprimir a tabuada de Divisao')
    print('4 --> Imprimir a tabuada de Multiplicacao')
    print('5 --> Sair\n')

    n = int(input('Entre com alguma das opcoes acima:'))

    if n == 5:

        break

    elif n == 1:

        for i in range(1,11):
            print('Tabuada do', i)
            for j in range(1,11):
                print('%d + %d = %d' %(i, j, (i + j)))
            print('------------')

    elif n == 2:

        for i in range(1,11):
            print('Tabuada do', i)
            for j in range(1,11):
                print('%d - %d = %d' %(i, j, (i - j)))
            print('------------')

    elif n == 3:

        for i in range(1,11):
            print('Tabuada do', i)
            for j in range(1,11):
                print('%d / %d = %d' %(i, j, (i / j)))
            print('------------')

    elif n == 4:

        for i in range(1,11):
            print('Tabuada do', i)
            for j in range(1,11):
                print('%d * %d = %d' %(i, j, (i * j)))
            print('------------')

    else:
        print('Opcao invalida ! ')




    
'''

13) Escreva um programa que leia números inteiros do teclado. O programa deve ler os números 
    até que o usuário digite 0 (zero). No final da execução, exiba a quantidade de números digitados,
    assim como a soma e a média aritmética
'''

quantidade = 0
soma = 0

while True:
    n = int(input('Informe um numero inteiro: '))
    
    if n == 0:
        break
    else:
        quantidade += 1
        soma += n

print(f'\nVoce digitou {quantidade} numero(s)')
print(f'A soma dos numeros que foram digitados eh {soma}')
print(f'A Media aritmetica dos numeros que foram digitados eh {soma / quantidade}')
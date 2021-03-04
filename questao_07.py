'''
7) Escreva um programa que leia dois números. Imprima o resultado da multiplicação do primeiro pelo 
   segundo. Utilize apenas os operadores de soma e subtração para calcular o resultado. 
   Lembre-se de que podemos entender a multiplicação de dois números como somas sucessivas 
   de um deles. Assim, 4 × 5 = 5 + 5 + 5 + 5 = 4 + 4 + 4 + 4 + 4.
'''

num_01 = int(input('Informe o primeiro numero: '))
num_02 = int(input('Informe o segundo numero: '))
multiplicação = 0

if num_01 < 0 and num_02 < 0: 
    
    for valor in range(num_01 * -1):
        multiplicação -= num_02    

elif num_01 < 0: 

    for valor in range(num_02):
        multiplicação += num_01

else:

    for valor in range(num_01):
        multiplicação += num_02


print('%d x %d = %d' %(num_01, num_02, multiplicação))
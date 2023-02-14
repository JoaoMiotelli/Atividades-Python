# 16. Crie um programa que leia 5 números inteiros, coloque-os em uma lista e moste cada número juntamente com sua posição na lista.

num1 = input('Informe o valor de um número: ')
num2 = input('Informe o valor de um segundo número: ')
num3 = input('Informe o valor de um terceiro número: ')
num4 = input('Informe o valor de um quarto número: ')
num5 = input('Informe o valor de um quinto número: ')


lista = [num1,num2,num3,num4,num5]
print(lista)
print('Posição 0: %s \nPosição 1: %s \nPosição 2: %s \nPosição 3: %s \nPosição 4: %s' %(num1,num2,num3,num4,num5))
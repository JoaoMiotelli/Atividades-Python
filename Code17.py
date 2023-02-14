# 17. Crie um programa que leia 3 números inteiros em duas listas L1 e L2. Em seguida, concatene em uma nova lista L3 imprima a lista L3 ordenada de maneira crescente e decrescente.

num1_1 = input('Informe o valor de um número para ser aderido a uma lista: ')
num1_2 = input('Informe o valor de um segundo número para ser aderido a uma lista: ')
num1_3 = input('Informe o valor de um tercerio número para ser aderido a uma lista: ')
num2_1 = input('\nInforme o valor de um número para ser aderido a uma segunda lista: ')
num2_2 = input('Informe o valor de um segundo número para ser aderido a uma segunda lista: ')
num2_3 = input('Informe o valor de um terceiro número para ser aderido a uma segunda lista: ')
l1 = [num1_1,num1_2,num1_3]
l2 = [num2_1,num2_2,num2_3]
l3 = l1 + l2

print(l3)
l3.sort(reverse=True)
print(l3)
l3.sort(reverse=False)
print(l3)
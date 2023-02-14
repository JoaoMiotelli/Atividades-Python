# 10. Crie um programa que receba um número inteiro n, correspondente a um valor em reais. O programa deve calcular a quantidade mínima de notas de 100, 50, 10 e 1 necessárias para que um caixa eletrônico consiga fornecer o valor.

valReais = float(input('Informe o valor em reais a serem sacados: '))

qt100 = valReais // 100
resto100 = valReais % 100
qt50 = resto100 // 50
resto50 = resto100 % 50
qt10 = resto50 // 10
resto10 = resto50 % 10
qt1 =  resto10 // 1

print('Total de %.0f de R$100' %(qt100))
print('Total de %.0f de R$50' %(qt50))
print('Total de %.0f de R$10' %(qt10))
print('Total de %.0f de R$1' %(qt1))
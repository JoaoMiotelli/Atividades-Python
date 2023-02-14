# 9. Faça um programa que receba dois valores do tipo inteiro x e y, calcule e imprima o valor de z conforme a equação: z = \frac(x^2 + y^2)(x - y)

valX = int(input('Informe um valor inteiro para X: '))
valY = int(input('Informe um valor inteiro para Y: '))
valZ = (valX**2 + valY**2)//(valX - valY)

print('O valor obtido a partir dos cálculos efetuados é de', valZ)
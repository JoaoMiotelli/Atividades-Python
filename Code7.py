# 7. Faça um programa que calcule e imprima o valor da hipotenusa de um triângulo retângulo, cujos catetos são fornecidos pelo usuário.

cateto1 = float(input('Informe o valor de um dos catetos '))
cateto2 = float(input('Informe o valor do outro do cateto '))
hipotenusa = (cateto1**2 + cateto2**2)
resultado = hipotenusa ** (0.5)

print('O valor da hipotenusa do triângulo retangulo é %.2f' %resultado)
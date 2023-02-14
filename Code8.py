# 8. Um triângulo equilátero é um triangulo que possui medidas iguais. Faça um programa onde o usuário forneça as medidas dos lados A, B e C de um triângulo e o programa informe se é um triângulo equilátero ( True ou False ).

print('Informe os valores do lado de um triângulo é verifique se ele é um triângulo equilátero. \n')
lado1 = float(input('Informe o valor do primeiro lado: '))
lado2 = float(input('Informe o valor do segundo lado: '))
lado3 = float(input('Informe o valor do terceiro lado: '))

print((lado1 == lado2)and(lado2 == lado3)and(lado3 == lado1))
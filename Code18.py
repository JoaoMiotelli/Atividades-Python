# 18. Desenvolva um programa que solicite o nome e a idade de 5 pessoas e armazene cada informação em uma respectiva lista. Então, imprima o nome e a idade na ordem inversa a ordem lida.

nome1 = input('Informe o seu nome: ')
idade1 = input('Informe sua idade: ')
nome2 = input('Informe o nome de um familiar: ')
idade2 = input('Informe a idade desse familiar: ')
nome3 = input('Informe o nome de um conhecido: ')
idade3 = input('Informe a idade desse conhecido: ')
nome4 = input('Informe o nome de um colega de trabalho: ')
idade4 = input('Informe a idade desse colega: ')
nome5 = input('Informe o nome de um amigo virtual: ')
idade5 = input('Informe a idade desse amigo: ')

lista_1 = [nome1,idade1]
lista_2 = [nome2,idade2]
lista_3 = [nome3,idade3]
lista_4 = [nome4,idade4]
lista_5 = [nome5,idade5]

print('\n%s \n%s \n%s \n%s \n%s'%(lista_1,lista_2,lista_3,lista_4,lista_5))
lista_1.sort(reverse=False)
lista_2.sort(reverse=False)
lista_3.sort(reverse=False)
lista_4.sort(reverse=False)
lista_5.sort(reverse=False)
print('\n%s \n%s \n%s \n%s \n%s'%(lista_1,lista_2,lista_3,lista_4,lista_5))
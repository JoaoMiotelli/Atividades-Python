# 1. Faça um programa em Python que solicite as três notas tiradas por vocês na disciplina de programação e imprima no console as notas e a média das notas.

nota1 = float(input('Entre com a nota da sua primeira prova de Programação: '))
nota2 = float(input('Entre com a nota da sua segunda prova de Programação: '))
nota3 = float(input('Entre com a nota da sua terceira prova de Programação: '))
print('A media das notas é: ', (nota1+nota2+nota3)/3)


# 2. Faça um programa em Python que receba o salário de um funcionário (do ano de 2021) e imprima o salário de 2022 reajustado conforme a inflação do ano de 2021 que foi de 10.06%

sal = float(input('Digite o salário adquirido no ano de 2021: '))
print("Seu salário em 2022, após o reajuste, devido a inflação é R$", sal+(sal*0.1006))


# 3. Faça um programa que leia o nome de um produto, a quantidade comprada e o valor unitário e imprima na tela o nome do produto e o valor total da venda.

nome = input('Informe o nome do poduto: ')
quant = int(input('Informe a quantidade de %s comprados: ' %nome))
val_unit = float(input('Informe o valor da unidade %s: ' %nome))
totalvendas = quant*val_unit

print('\n', nome)
print('Total de vendas é de %.2f' %totalvendas)


# 4. Faça um programa que transforma uma temperatura fornecida em Celsius para a correspondente em Fahrenheit. Faça uma pesquisa para encontrar a fóruma de conversão. C=9/5+(F−32)

print('Programa de Converção de °C em °F')
tempCelcius = float(input('Digite a temperatura em Celcius: '))
tempFahrenheit = (1.8*tempCelcius + 32)
print('A temperatura de %.2f°C equivale a %.2f°F'%(tempCelcius, tempFahrenheit))


# 5. Faça um programa que receba um valor referente a uma quantidade total em segundos, calcule e mostra quantas horas:minutos:segundos corresponde a quantidade total de segundo.

print('Digite uma quantidade em segundos que mostrara uo valor em horas:minutos:segundos')
segTotal = int(input('Digite a quantidade de segundos totais: '))

qtHoras = segTotal//3600
restoSegundos = segTotal%3600
qtMinutos = restoSegundos//60
qtSegundos = restoSegundos%60

print('\nA quantida de segundos equivale a %.02d:%.02d:%.02d'%(qtHoras,qtMinutos,qtSegundos))


# 6. Após a queda de um raio um observador anotou o tempo, em segundos, entre a luz e o som do raio. Considerando a velocidade do som igual a 340 m/s, faça um programa que receba o tempo medido por um observador e imprima a distância, em kilometros, do observador até o ponto de queda do raio.

tempo = float(input('Digite o tempo, em segundos, do som propagado: '))
metros = 340 * tempo
kilometros = metros // 1000

print('A distacia do observador em relação ao raio é %.2f km'%(kilometros))


# 7. Faça um programa que calcule e imprima o valor da hipotenusa de um triângulo retângulo, cujos catetos são fornecidos pelo usuário.

cateto1 = float(input('Informe o valor de um dos catetos '))
cateto2 = float(input('Informe o valor do outro do cateto '))
hipotenusa = (cateto1**2 + cateto2**2)
resultado = hipotenusa ** (0.5)

print('O valor da hipotenusa do triângulo retangulo é %.2f' %resultado)


# 8. Um triângulo equilátero é um triangulo que possui medidas iguais. Faça um programa onde o usuário forneça as medidas dos lados A, B e C de um triângulo e o programa informe se é um triângulo equilátero ( True ou False ).

print('Informe os valores do lado de um triângulo é verifique se ele é um triângulo equilátero. \n')
lado1 = float(input('Informe o valor do primeiro lado: '))
lado2 = float(input('Informe o valor do segundo lado: '))
lado3 = float(input('Informe o valor do terceiro lado: '))

print((lado1 == lado2)and(lado2 == lado3)and(lado3 == lado1))


# 9. Faça um programa que receba dois valores do tipo inteiro x e y, calcule e imprima o valor de z conforme a equação: z = \frac(x^2 + y^2)(x - y)

valX = int(input('Informe um valor inteiro para X: '))
valY = int(input('Informe um valor inteiro para Y: '))
valZ = (valX**2 + valY**2)//(valX - valY)

print('O valor obtido a partir dos cálculos efetuados é de', valZ)


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


# 11. Crie um programa que imprima o comprimento de uma string fornecida pelo usuário.

minhaString = input('Forneça uma frase qualquer para a determinação do tamanho da String: ')
tamanhoString = len(minhaString)

print('O tamanho da String é', tamanhoString)


# 12. Escreva um programa para verificar se a palavra 'laranja' está presente em "Isto é suco de laranja".

frase = "Isto é suco de laranja"

print("laranja" in frase)


# 13. Escreva um programa que solicite uma frase ao usuário e escreva a frase toda em maiúscula e sem espaços em branco (está sendo reconsiderado).

string = input('Escreva uma frase qualquer para conversão em maiuscula: ')
print('String normal: ', string)

stringMai = string.upper()
novaString = stringMai.replace(" ", "")
print('String maiúscula: ', novaString)


# 14. Faça um programa que dada duas strings, s1 e s2 retornam uma nova string composta do primeiro, do meio e dos últimos caracteres de cada string de entrada.

s1 = input('Informe uma palavra: ')
s2 = input('Informe outra palavra: ')

s3 = s1 + " " + s2
tamString1 = len(s1)
tamString2 = len(s2)
midString1 = tamString1//2
midString2 = tamString2//2
ultString1 = tamString1-1
ultString2 = tamString2-1

primCaract = (s1[0]) + (s2[0])
meioCaract = (s1[midString1]) + (s2[midString2])
ultiCaract = (s1[ultString1]) + (s2[ultString2])
novaString = primCaract + meioCaract + ultiCaract
print('\n', s3, primCaract, meioCaract, ultiCaract)
print('\n', novaString)


# 15. Dada uma frase fornecida pelo usuário faça um programa que encontre todas as ocorrências de "covid19", você pode ignorar a verificação de maiúsculas e minúsculas.

fraseUsuario = input('Informe, detalhadamente, as ocorrências de casos de covid19 em Santa Catarina e suas causas: ')
quantCovid1 = fraseUsuario.count('Covid19')
quantCovid2 = fraseUsuario.count('covid19')
quantCovid = quantCovid1 + quantCovid2

print('A quantidade de vezes que a palavra Covid19 foi citada no decorrer do texto é: ', quantCovid )


# 16. Crie um programa que leia 5 números inteiros, coloque-os em uma lista e moste cada número juntamente com sua posição na lista.

num1 = input('Informe o valor de um número: ')
num2 = input('Informe o valor de um segundo número: ')
num3 = input('Informe o valor de um terceiro número: ')
num4 = input('Informe o valor de um quarto número: ')
num5 = input('Informe o valor de um quinto número: ')


lista = [num1,num2,num3,num4,num5]
print(lista)
print('Posição 0: %s \nPosição 1: %s \nPosição 2: %s \nPosição 3: %s \nPosição 4: %s' %(num1,num2,num3,num4,num5))


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


# 19. Desenvolva um Script Python que conte quantas vezes um nome está presente em uma lista com 5 nomes diferentes e aleatórios. O programa deve armazenar essa contagem em um dicionário {'nome':x_vezes }

nome1 = input('Informe um nome qualquer: ')
nome2 = input('Informe outro nome qualquer ou o mesmo citado anteriormente: ')
nome3 = input('Informe outro nome qualquer ou o mesmo citado anteriormente: ')
nome4 = input('Informe outro nome qualquer ou o mesmo citado anteriormente: ')
nome5 = input('Informe outro nome qualquer ou o mesmo citado anteriormente: ')

lista = [nome1,nome2,nome3,nome4,nome5]
lista_1 = lista.count(nome1)
lista_2 = lista.count(nome2)
lista_3 = lista.count(nome3)
lista_4 = lista.count(nome4)
lista_5 = lista.count(nome5)
dic_1 = {nome1:lista_1}
dic_2 = {nome2:lista_2}
dic_3 = {nome3:lista_3}
dic_4 = {nome4:lista_4}
dic_5 = {nome5:lista_5}

print('\nQuantidade de vezes que os nomes citados aperecem')
print('\n%s\n%s\n%s\n%s\n%s' %(dic_1,dic_2,dic_3,dic_4,dic_5))


# 20. Crie um programa que cadastre as informações (nome, idade e CPF) de 3 pessoas e coloque em um dicionário. Então, imprima de forma organizada as informações do dicionário.

print('Programa de Cadastro de Usuário')
nome1 = input('Infome um nome de usuário: ')
idade1 = input('Informe a idade desse usuário: ')
cpf1 = input('Informe o CPF desse usuário: ')
nome2 = input('\nInfome um nome de usuário: ')
idade2 = input('Informe a idade desse usuário: ')
cpf2 = input('Informe o CPF desse usuário: ')
nome3 = input('\nInfome um nome de usuário: ')
idade3 = input('Informe a idade desse usuário: ')
cpf3 = input('Informe o CPF desse usuário: ')

dic_1 = {'Nome':nome1,'Idade':idade1, 'CPF':cpf1}
dic_2 = {'Nome':nome2,'Idade':idade2, 'CPF':cpf2}
dic_3 = {'Nome':nome3,'Idade':idade3, 'CPF':cpf3}
print('\n',dic_1)
print('\n',dic_2)
print('\n',dic_3)


# 21.

vl_imovel = float(input('Informe o valor do imóvel a ser comprado: '))
salario = float(input('Informe seu salário: '))
anos = int(input('Informe a quantidade de anos desejados a pagar: '))

vl_prestacao = vl_imovel/(anos*12)

if anos>30:
    print('O limite das prestações em anos foi excedido.')
else:
    if vl_prestacao>(salario*0.3):
        print(f'O empréstimo não poderá ser efetivado, pois o valor da prestação, efetiva em {anos} ano(s), é superior a mais de 30% do salário informado.')
    else:
        print('O empréstimo poderá ser efetivado. O valor da prestação mensal a ser paga é de R$%.2f em um período de %d ano(s).'%(vl_prestacao, anos))
# 3. Faça um programa que leia o nome de um produto, a quantidade comprada e o valor unitário e imprima na tela o nome do produto e o valor total da venda.

nome = input('Informe o nome do poduto: ')
quant = int(input('Informe a quantidade de %s comprados: ' %nome))
val_unit = float(input('Informe o valor da unidade %s: ' %nome))
totalvendas = quant*val_unit

print('\n', nome)
print('Total de vendas é de %.2f' %totalvendas)
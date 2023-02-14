# 5. Faça um programa que receba um valor referente a uma quantidade total em segundos, calcule e mostra quantas horas:minutos:segundos corresponde a quantidade total de segundo.

print('Digite uma quantidade em segundos que mostrara uo valor em horas:minutos:segundos')
segTotal = int(input('Digite a quantidade de segundos totais: '))

qtHoras = segTotal//3600
restoSegundos = segTotal%3600
qtMinutos = restoSegundos//60
qtSegundos = restoSegundos%60

print('\nA quantida de segundos equivale a %.02d:%.02d:%.02d'%(qtHoras,qtMinutos,qtSegundos))
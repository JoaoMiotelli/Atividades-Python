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
# 15. Dada uma frase fornecida pelo usuário faça um programa que encontre todas as ocorrências de "covid19", você pode ignorar a verificação de maiúsculas e minúsculas.

fraseUsuario = input('Informe, detalhadamente, as ocorrências de casos de covid19 em Santa Catarina e suas causas: ')
quantCovid1 = fraseUsuario.count('Covid19')
quantCovid2 = fraseUsuario.count('covid19')
quantCovid = quantCovid1 + quantCovid2

print('A quantidade de vezes que a palavra Covid19 foi citada no decorrer do texto é: ', quantCovid )
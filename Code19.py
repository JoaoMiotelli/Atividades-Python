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
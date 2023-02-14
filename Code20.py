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
# 13. Escreva um programa que solicite uma frase ao usuário e escreva a frase toda em maiúscula e sem espaços em branco (está sendo reconsiderado).

string = input('Escreva uma frase qualquer para conversão em maiuscula: ')
print('String normal: ', string)

stringMai = string.upper()
novaString = stringMai.replace(" ", "")
print('String maiúscula: ', novaString)
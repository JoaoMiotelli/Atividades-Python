# 2. Faça um programa em Python que receba o salário de um funcionário (do ano de 2021) e imprima o salário de 2022 reajustado conforme a inflação do ano de 2021 que foi de 10.06%

sal = float(input('Digite o salário adquirido no ano de 2021: '))
print("Seu salário em 2022, após o reajuste, devido a inflação é R$", sal+(sal*0.1006))
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
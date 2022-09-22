preco = float(input('Qual o valor do imovél? R$'))
sal = float(input('Qual sua renda mensal ? R$'))
ano = int(input('Quantos anos de financiamento ? R$'))
prestacao = preco / (ano * 12)
print('Para pagar uma casa no valor de R${:.2f} em {} anos a prestação séra de R${:.2f} '.format(preco, ano, prestacao))

if prestacao > (sal * 0.30):
    print('Emprestimo NEGADO')
else:
    print('Emprestimo APROVADO')

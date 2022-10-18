# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o
# valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30%
# do salário ou então o empréstimo será negado.

preco = float(input('Qual o valor do imovél? R$'))
sal = float(input('Qual sua renda mensal ? R$'))
ano = int(input('Quantos anos de financiamento ? R$'))
prestacao = preco / (ano * 12)
print('Para pagar uma casa no valor de R${:.2f} em {} anos a prestação séra de R${:.2f} '.format(preco, ano, prestacao))

if prestacao > (sal * 0.30):
    print('Emprestimo NEGADO')
else:
    print('Emprestimo APROVADO')

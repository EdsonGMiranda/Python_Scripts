# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando
# o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – em 3x ou mais no cartão: 20% de juros
prc_produto = float(input('Entre com o valor do produto R$:'))
print('Qual a forma de pagamento? ')
print('[1] à vista dinheiro/cheque ')
print('[2] à vista no cartão ')
print('[3] em até 2x no cartão ')
print('[4] em 3x ou mais no cartão ')
opc = int(input('Escolha :'))
if opc == 1:
    print('A forma de pagamento é a vista no dinheiro/cheque ')
    prc_final = prc_produto - (prc_produto * 0.10)
    print('O valor do produto com desconto ficou R${}'.format(prc_final))
elif opc == 2:
    print('A forma de pagamento é a vista no cartão ')
    prc_final = prc_produto - (prc_produto * 0.05)
    print('O valor do produto com desconto ficou R${}'.format(prc_final))
elif opc == 3:
    print('A forma de pagamento é em x2 no cartão ')
    prc_final = prc_produto
    print('O valor do produto não teve desconto é o preço é R${}'.format(prc_final))
    print('O valor das parcelas é {}'.format(prc_final/2))
elif opc == 4:
    print('A forma de pagamento é em x3 ou mais no cartão ')
    parcelas = int(input('Qual o numero de parcelas? '))
    prc_final = prc_produto + (prc_produto * 0.20)
    print('O valor do produto com juros ficou R${}'.format(prc_final))
    print('O seu parcelamento é de {}x é o valor das parcelas é {}'.format(parcelas, prc_final/parcelas))
else:
    print('Opção inválida ')

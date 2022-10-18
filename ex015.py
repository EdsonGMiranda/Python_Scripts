# Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar,
# sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input('Por quantos dias você você alugou o carro? '))
km = float(input('Quantos KM''s você rodou com o carro? '))
total = (dias * 60) + (km * 0.15)
print('O total a pagar é R${:.2f}'.format(total))
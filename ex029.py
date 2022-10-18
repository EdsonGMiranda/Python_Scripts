# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Entre com a velocidade do carro em Km: '))
if velocidade > 80:
    print('Você foi multado por andar a {}KM/h em uma area onde o limite de velocidade é 80KM/h'.format(velocidade))
    print('O valor da sua multa é R${:.2f}'.format((velocidade - 80)*7))

else:
    print('sua velocidade é {}KM/h dentro do limite de velocidade'.format(velocidade))

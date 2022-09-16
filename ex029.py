velocidade = float(input('Entre com a velocidade do carro em Km: '))
if velocidade > 80:
    print('Você foi multado por andar a {}KM/h em uma area onde o limite de velocidade é 80KM/h'.format(velocidade))
    print('O valor da sua multa é R${:.2f}'.format((velocidade - 80)*7))

else:
    print('sua velocidade é {}KM/h dentro do limite de velocidade'.format(velocidade))

# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = float(input('Entre com a distancia da sua viagem: '))
taxa1 = float(0.50)
taxa2 = float(0.45)
print('Sua viagem de {}KM'.format(distancia))
if distancia <= 200:
    print('O custo da passagem é  R${:.2f}'.format(distancia * taxa1))
else:
    print('O custo da passagem é  R${:.2f}'.format(distancia * taxa2))



# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date, datetime
data_atual = date.today()
menor = 0
maior = 0
for i in range(0, 7):
    dtnasc_inp = input('Entre com a data de nascimento (ex:01/01/2001): ')
    dtnasc = datetime.strptime(dtnasc_inp, '%d/%m/%Y').date()
    idade = data_atual.year - dtnasc.year - ((data_atual.month, data_atual.day) < (dtnasc.month, dtnasc.day))
    if idade < 18:
        menor += 1
    elif idade >= 18:
        maior += 1
print('{} pessoas são menores de idade, e {} são maiores de idade'.format(menor, maior))

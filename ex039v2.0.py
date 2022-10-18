# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
# Usando alguma manipulação de datas.

from datetime import date,datetime

dtnasc_inp = input('Entre com de nascimento: ex: 01/01/2022: ')
dtnasc = datetime.strptime(dtnasc_inp, '%d/%m/%Y').date()
data_atual = date.today()
idade = data_atual.year - dtnasc.year -((data_atual.month,data_atual.day) < (dtnasc.month, dtnasc.day))
if idade < 18:
     print('Você ainda não se alistou')
     print('faltam {} ano(s) para você se alistar'.format(18 - idade))
elif idade > 18:
    print('Você já se alistou')
    print('Você se alistou a {} ano(s)'.format(idade - 18))
elif idade == 18:
    print('Você está no ano de se alistar')



print(idade)
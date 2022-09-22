from datetime import date
dtnasc = int(input('Entre com de nascimento: '))
data_atual = date.today()
idade = int(data_atual.year) - dtnasc
if idade < 18:
    print('Você ainda não se alistou')
    print('faltam {} ano(s) para você se alistar'.format(18 - idade))
elif idade > 18:
    print('Você já se alistou')
    print('Você se alistou a {} ano(s)'.format(idade - 18))
elif idade == 18:
    print('Você está no ano de se alistar')



print(idade)
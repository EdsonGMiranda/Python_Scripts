# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia
# o ano de nascimento de um atleta e mostre sua  categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date
dtnasc = int(input('Entre com o ano de nascimento do atleta: '))
data_atual = date.today()
idade = int(data_atual.year) - dtnasc
if idade <= 9:
    print('O atleta tem {} anos e sua categoria é MIRIM'.format(idade))
elif idade <= 14:
    print('O atleta tem {} anos e sua categoria é INFANTIL'.format(idade))
elif idade <= 19:
    print('O atleta tem {} anos e sua categoria é JÚNIOR'.format(idade))
elif idade <= 25:
    print('O atleta tem {} anos e sua categoria é SÊNIOR'.format(idade))
else:
    print('O atleta tem {} anos e sua categoria é MASTER'.format(idade))


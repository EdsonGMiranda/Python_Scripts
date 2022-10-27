# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
# o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa
# tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(dt_nasc):
    from datetime import date
    dt_atual = date.today().year
    idade = dt_atual - dt_nasc
    if 16 <= idade < 18 or idade > 65:
        return f'Você possui {idade} anos e o voto É OPCIONAL.'
    elif idade > 18:
        return f'Você possui {idade} anos e o voto É OBRIGATÓRIO.'
    elif idade < 16:
        return f'Você possui {idade} anos e o voto NÃO OBRIGATÓRIO.'


print(voto(1952))
print('-' * 20)
print(voto(2016))
print('-' * 20)
print(voto(1988))
print('-' * 20)
nasc = int(input('Entre com a data de nascimento: '))
print(voto(nasc))





# Exercício Python 092: crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário
# receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos
# anos a pessoa vai se aposentar.

from datetime import date

# Entradas
pessoa = dict()
nome = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
ctps = int(input('Carteira de Trabalho: (0 não tem) '))
# variavéis implicitas
ano = date.today().year
idade = ano - ano_nascimento
if ctps != 0:
    ano_contra = int(input('Ano contratação: '))
    sal = float(input('Salario: '))

    # variavéis implicitas
    temp_job = ano - ano_contra
    apos = idade + (35 - temp_job)

    # criação do dicionário
    pessoa['Nome'] = nome
    pessoa['Idade'] = idade
    pessoa['CTPS'] = ctps
    pessoa['Ano-Contratação'] = ano_contra
    pessoa['Salario'] = sal
    pessoa['Aposenta'] = apos
else:
    # criação do dicionário
    pessoa['Nome'] = nome
    pessoa['Idade'] = idade
    pessoa['CTPS'] = ctps

print('-=' * 20)
for k, v in pessoa.items():
    print(f'- {k} tem o valor {v}')



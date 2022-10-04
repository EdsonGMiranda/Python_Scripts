# Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

count = c_homem = c_maior18 = c_mulher_20 = 0
sair = ' '
while True:
    print('-=-' * 10)
    print(f'Entre com a {count + 1} pessoa ')
    print('-=-' * 10)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: ')).upper().strip()[0]
    if idade > 18:
        c_maior18 += 1
    if sexo == 'M':
        c_homem += 1
    if sexo == 'F' and idade < 20:
        c_mulher_20 +=1
    sair = ' '
    while sair not in 'SN':
        sair = str(input('Desaja continuar? [S/N]')).upper().strip()[0]
    if sair == 'N':
        break
    count += 1
print(f'Foram cadastrados {c_maior18} maiores de idade ')
print(f'Foram cadastrados {c_homem} homens ')
print(f'Foram cadastradas {c_mulher_20} mulheres menores de 20 ')

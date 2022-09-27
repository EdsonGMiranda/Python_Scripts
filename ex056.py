# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
s_media = 0
mais_velho = 0
n_m_velho = ''
count = 0
for i in range(1, 5):
    print('-----------{}ª Pessoa -------------'.format(i))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]'.format(i)).upper().split()
    s_media += idade
    if sexo == 'M':
        if idade > mais_velho:
            n_m_velho = nome
    elif sexo == 'F':
        if idade < 20:
            count += 1
media = s_media / i
print('A média da idade do grupo é {} anos'.format(media))
print('O nome do homem mais velhor é {}'.format(n_m_velho))
print('Existem {} mulheres menores de 20 anos de idade'.format(count))
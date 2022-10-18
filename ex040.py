# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem
# no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

nota1 = float(input('Entre com a nota do primeiro semestre: '))
nota2 = float(input('Entre com a nota do segundo semestre: '))
media = (nota1 + nota2) / 2
if media >= 7:
    print('Sua média foi {:.1f} você foi APROVADO '.format(media))
elif media >= 5 and media <= 6.9:
    print('Sua média foi {:.1f} você está de RECUPERAÇÃo'.format(media))
else:
    print('Sua média foi {:.1f} você está REPROVADO'.format(media))


# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa
# Corporal (IMC)e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

peso = float(input('Entre com o peso (KG):'))
altura = float(input('Entre com a altura (m):'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu imc é {:.1f} você está com ABAIXO DO PESO'.format(imc))
elif imc < 25:
    print('Seu imc é {:.1f} você está com PESO IDEAL'.format(imc))
elif imc < 30:
    print('Seu imc é {:.1f} você está com SOBREPESO'.format(imc))
elif imc < 40:
    print('Seu imc é {:.1f} você está com OBESIDADE'.format(imc))
else:
    print('Seu imc é {:.1f} você está com OBESIDADE MÓRBIDA'.format(imc))
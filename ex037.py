num = int(input('Digite um numero inteiro:'))
print('Escolha umas das bases para conversão')
print('[1] Converter para BINARIO')
print('[2] Converter para OCTAL')
print('[3] Converter para HEXADECIMAL')
escolha = int(input('Sua opção: '))
if escolha == 1:
    convertido = str(bin(num))
    print ('O numero {} convertido para BINARIO é : {}'.format(num, convertido[2:]))
elif escolha == 2:
    convertido = str(oct(num))
    print('O numero {} convertido para OCTAL é : {}'.format(num, convertido[2:]))
elif escolha == 3:
    convertido= str(hex(num))
    print('O numero {} convertido para HEXADECIMAL é : {}'.format(num, convertido[2:]))
else:
    print('Opção invalida')


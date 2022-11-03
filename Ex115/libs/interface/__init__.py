def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print(f'\033[31mERRO! Digite um numero inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print(f'\n\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for i in lista:
        print(f'\033[93m{c}-\033[m \033[31m{i}\033[m')
        c += 1
    opc = leiaint('Escoha a opção: ')
    return opc






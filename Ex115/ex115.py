from Ex115.libs.interface import *
from time import sleep
from Ex115.libs.arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criaarquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar novas pessoas', 'Sair do sistema'])
    if resposta == 1:
        cabecalho('LISTAR PESSOAS CADASTRADAS')
        lerarquivo(arq)
    elif resposta == 2:
        cabecalho('CADASTRAR NOVA PESSOA')

        while True:
            nome = str(input('Nome: '))
            idade = leiaint('Idade: ')
            cadatrarpessoa(arq, nome, idade)
            sair = input('Deseja continuar? [S/N]').strip().upper()[0]
            if sair == 'N':
                break

    elif resposta == 3:
        cabecalho('Saindo do sistema ... até logo!')
        break
    else:
        print('Error digite um opção valida!')
    sleep(2)





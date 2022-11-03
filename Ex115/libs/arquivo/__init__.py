from Ex115.libs.interface import *


def criaarquivo(path):
    try:
        arquivo = open(path, "wt+")
        arquivo.close()
    except:
        print(f'Houve um erro na criação do {arquivo} .')
    else:
        print(f'O arquivo {arquivo} foi criado com sucesso!')


def arquivoexiste(path):
    try:
        a = open(path, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def lerarquivo(path):
    try:
        arquivo = open(path, 'rt')
    except:
        print('Error ao ler o arquivo!')
    else:
        cabecalho('Pessoas cadastradas')
        for l in arquivo:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', ' ')
            print(f'{dado[0]:<30}{dado[1]:>3}anos')

    finally:
        arquivo.close()


def cadatrarpessoa(path, nome='desconhecido', idade=0):
    try:
        arquivo = open(path, 'at')
    except:
        print(f'Houve erro na abertura do arquivo {path}.')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever os dados.')
        else:
            print(f'Novo registro de {nome} foi cadastrado com suceso.')
        finally:
            arquivo.close()





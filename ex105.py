# Exercício Python 105: Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor
# – A média da turma
# – A situação (opcional)


def notas(* n, sit=False):
    """
    :param n: uma ou mais notas de alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adcionar situação.
    :return: dicionarios com várias informações sobre situação da turma.
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n)/len(n)

    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'

    return r


resp = notas(8, 7.5, 6.5, 7, 4, 9,  sit=True)
print(resp)
help(notas)

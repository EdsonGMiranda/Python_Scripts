# Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo computador usado.

def testpudim(url):
    import urllib.request
    try:
        site = urllib.request.urlopen(url)
    except Exception as erro:
        print(f'Servidor indisponibel error {erro}')
    else:
        print('Tudo OK')
        print(site.read())


print(testpudim('http://www.pudim.com.br/'))

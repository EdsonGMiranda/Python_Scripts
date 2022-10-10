import pandas as pd


#base = pd.read_csv('2022Atracacao.csv', encoding='latin-1',sep=';',header=1)
# IDAtracacao	CDTUP	IDBerco	Berço	Porto Atracação	Apelido Instalação Portuária	Complexo Portuário	Tipo da Autoridade
# Portuária	Data Atracação	Data Chegada	Data Desatracação	Data Início Operação	Data Término Operação
# Ano	Mes	Tipo de Operação	Tipo de Navegação da Atracação	Nacionalidade do Armador	FlagMCOperacaoAtracacao	Terminal
# Município	UF	SGUF	Região Geográfica	Nº da Capitania	Nº do IMO


base = pd.read_csv('2022Atracacao.csv', encoding='latin-1', sep=';', header=0)
df1 = base.dropna(thresh=18)
for i in range(0,20):
    lin = df1.iloc[i]
    print('-=' * 50)
    print(lin)
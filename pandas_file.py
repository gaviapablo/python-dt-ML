import numpy as np
import pandas as pd

#series
#pensar neles como se fossem dicionarios, com chave e valor
labels = ['a','b','c']

my_list = [10,20,30]
arr = np.array(my_list)

d = { 'a' : 10, 'b' : 20, 'c' : 30}

series = pd.Series(data=my_list, index=labels)
series_np = pd.Series(arr,labels)
#funciona tanto para listas quanto para arrays do numpy (series=series_np)
#indexação tambem funciona nesse caso
series_primeiro_valor = series['a']

#ideia das series é fazer operações baseadas no índice
series_1 = pd.Series([1,2,3,4],['EUA','Alemanha','Chile','Argentina'])
series_2 = pd.Series([1,2,3,4],['EUA','Rússia','Chile','Argentina'])
#ele soma o valor de cada índice se encontrados nas duas séries, caso nao sejam encontrados os indices
#nas duas series, retorna NaN -> Argentina = 8, Chile = 6, EUA = 2, Alemanha e Rússia com NaN

np.random.seed(101)
df = pd.DataFrame(np.random.randn(5,4), index='A B C D E'.split(), columns='W X Y Z'.split())
print(df)
print("\n")
#inspecionando elementos do dataframe
df.loc['E','W'] #devolve elemento individual
df.loc['E'].to_frame().T #devolve linha em formato de series, to_frame().T para fazer a transposição e printar em 
                         #formato de linha e nao de coluna.

df.loc[['A','E'],['W','Z']] #pegar uma fatia do dataFrame

df.iloc[:2,2:] #posso usar indices dos arrays numpy ao inves dos indices criados pelo index



#criando coluna nova
df['nova_coluna'] = df['W'] - df['Y']



#remove elementos ou linhas colunas inteiras. axis = 1 p remover coluna, axis = 0 p/ default p linha
#inplace=True mexe diretamente no dataFrame, nao cria uma copia com uma coluna dropada
df.drop('E',inplace=False)

#comparações retornam um dataframe de mesmo tamanho com as comparações feitas em cada elemento
bol = df > 0

#utilizando notação de colchetes podemos retirar elementos do dataframe com base em condições
df_positive = df[bol]

#o que da pra fazer com notação de colchetes é selecionar fatias do dataframe com base em condições
#nesse caso, a linha 'C' é retirada por ser a unica da coluna 'W' com valor negativo
df[df['W']>0]

#nesse caso, retornamos a coluna 'Y' menos a linha que em 'W' era menor que zero
df[df['W']>0]['Y']

#utilizando multiplas condições
#aplica as duas condições, qualquer linha de W que for menor q zero e qualquer linha de Z maior que zero são removidas 
df[(df['W']>0) & (df['Z']>0.6)]
#só remove uma linha caso as duas condições forem satisfeitas sobre a linha ao mesmo tempo
df[(df['W']>0) | (df['Z']>0.6)]

#reseta os indices das linhas para os indices padrões do array do numpy (0,1,2,3...) caso não sejam incluidos parametros
#e transforma a antiga coluna de índices em uma coluna normal com o nome de coluna "index"
#inplace também funciona aqui
df.reset_index()


#set_index serve para setar uma das colunas existentes como index de linhas
coluna = 'RJ SP SC MG RS'.split()
df['Estado'] = coluna
df.set_index('Estado', inplace=True)





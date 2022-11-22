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

#inspecionando elementos do dataframe
df.loc['E','W'] #devolve elemento individual
df.loc['E'] #devolve linha em formato de series

df.loc[['A','E'],['W','Z']] #pegar uma fatia do dataFrame

df.iloc[:2,2:] #posso usar indices dos arrays numpy ao inves dos indices criados pelo index



#criando coluna nova
df['nova_coluna'] = df['W'] - df['Y']



#remove elementos ou linhas colunas inteiras. axis = 1 p remover coluna, axis = 0 p/ default p linha
#inplace mexe diretamente no dataFrame, nao cria uma copia com uma coluna dropada
df.drop('E',inplace=True)

print(df)





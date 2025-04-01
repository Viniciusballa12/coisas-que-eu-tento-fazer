# Estudos DataFrame
import pandas as pd

# Lista: Uma coleção ordenada de elementos que podem ser de qualquer tipo
lista_nomes = ['Vinicius', 'Felipe' 'Carlos']
print('Lista de nomes: \n', lista_nomes)
print('Primeiro elemento na lista \n', lista_nomes[0])

# Dicionario: Estruturas composta de pares chave-valor
dicionario_pessoa = {
    'nome' : 'Vinicius',
    'idade' : 18,
    'cidade' : 'Nova Serrana'
}
print('Dicionario de uma pessoa: \n', dicionario_pessoa)
print('Atributo do Dicionario: \n', dicionario_pessoa.get('nome'))

# Lista de dicionarios: Estruturas de dados que combina listas e dicionarios
dados = [
    {'nome': 'Vinicius', 'idade': 18, 'cidade': 'Nova Serrana'},
    {'nome': 'Felipe', 'idade': 18, 'cidade': 'Divinópolis'},
    {'nome': 'Carlos', 'idade': 18, 'cidade': 'Paineiras'}
]

#DataFrame: Estruturas de dados bidimensionais
df = pd.DataFrame(dados)
print('DataFrame \n', df)

#selecionar coluna
print(df['nome'])

#selecionar varias colunas
print(df[['nome', 'idade']])

#selecionar linhas pelos indices
print('Primeira Linha \n', df.iloc[0])

#Adicionar uma nova coluna

df['salario'] = [2000, 1400, 1800]

#Adicionar um novo registro
df.loc[len(df)] = {
    'nome': 'Duda',
    'idade': 16,
    'cidade': 'Nova Serrana',
    'salario': 3200
}
print('DataFrame Atual \n', df)

#removendo uma coluna
df.drop('salario', axis=1, inplace=True)

#Filtrando pessoas com menos de 18
filtro_idade = df[df['idade'] <= 17]
print('Filtro \n', filtro_idade)

#Salvando o DataFrame em um arquivo CSV
df.to_csv('dados.csv', index=False)

#lendo um arquivo CSV em um DataFrame
df_lido = pd.read_csv('dados.csv')
print('\n Leitura do CSV \n', df_lido)











import pandas as pd

df = pd.read_csv('clientes1.csv')

pd.set_option('display.width', None)
print(df.head())

#Remover Dados
df.drop('pais', axis=1, inplace=True) #Coluna
df.drop(2, axis=0, inplace=True) #Linha

#Normalizar campo de texto
df['nome'] = df['nome'].str.title()
df['endereco'] = df['endereco'].str.lower()
df['estado'] = df['estado'].str.strip().str.upper()

#converter tipós de dados
df['idade'] = df['idade'].astype(int)

print('normalizar textos', df.head())

#Tratar valores nulos
df_fillna = df.fillna(0)
df_dropna = df.dropna()
df_dropna4 = df.dropna(thresh=4)
df = df.dropna(subset=['cpf'])

print('valores nulos \n', df.isnull().sum())
print('Qtd de registros nulos com fillna', df_fillna.isnull().sum().sum())
print('Qtd de registros nulos com dropna', df_dropna.isnull().sum().sum())
print('Qts de registros nulos com dropna4', df_dropna4.isnull().sum().sum())
print('Qtd de registros nulos com CPF', df.isnull().sum().sum())

df.fillna(  {'estados': 'Desconhecido'}, inplace=True)
df['endereco'] = df['endereco'].fillna('endereço informado')
df['idade_corrigida'] = df['idade'].fillna(df['idade'].mean())

#Tratar formato de dados
df['data_corrigida'] = pd.to_datetime(df['data'], format='%d/%m/%Y', errors='coerce')

#tratar formato de dados
print('Qtd registros atual:', df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset='cpf', inplace=True)
print('Qtd registros removendo as duplicadas', len(df))

print('Dados Limpos\n', df)

#Salvar DataFrame
df['data'] = df['data_corrigida']
df['idade'] = df['idade_corrigida']

df_salvar = df[['nome', 'cpf', 'idade', 'data', 'endereco', 'estado']]
df_salvar.to_csv('cliente_limpeza.csv', index=False)

print('Nova DataFrame: \n', pd.read_csv('clientes_limpeza.csv'))



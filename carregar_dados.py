import pandas as pd

# Carregar os dados
df_treino = pd.read_csv("treino.csv")  # Substitua pelo caminho correto se necessário
df_teste = pd.read_csv("teste.csv")  # Substitua pelo caminho correto se necessário

# Exibir as primeiras linhas dos arquivos
print("Dados de Treino:")
print(df_treino.head())  # Mostra as 5 primeiras linhas

print("\nInformações do conjunto de treino:")
print(df_treino.info())  # Exibe informações sobre as colunas

print("\nDados de Teste:")
print(df_teste.head())  # Mostra as 5 primeiras linhas

# python carregar_dados.py
# import pandas as pd

# Carregar os dados
#df = pd.read_csv('treino.csv')

# Exibir as primeiras linhas para garantir que os dados foram carregados corretamente
# print(df.head())

import pandas as pd

# Carregar os dados
df = pd.read_csv('treino.csv')

# Exibir as primeiras linhas para garantir que os dados foram carregados corretamente
print(df.head())

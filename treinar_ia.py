# Código para treinar a IA
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score

# Carregar os dados
df_treino = pd.read_csv("treino.csv")
df_teste = pd.read_csv("teste.csv")

# Separar as features (X) e o target (y)
X = df_treino.drop(columns=["id", "target"])  # Remove ID e target
y = df_treino["target"]

# Dividir os dados em treino (80%) e validação (20%)
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

# Criar e treinar o modelo
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

# Fazer previsões na validação
y_pred = modelo.predict(X_val)

# Avaliar o modelo com F1-score
f1 = f1_score(y_val, y_pred, average="macro")
print(f"F1-score na validação: {f1:.4f}")

# Fazer previsões no conjunto de teste
X_teste = df_teste.drop(columns=["id"])  # Remove apenas o ID
y_teste_pred = modelo.predict(X_teste)

# Criar DataFrame para submissão
df_submissao = pd.DataFrame({"id": df_teste["id"], "target": y_teste_pred})

# Salvar o resultado em CSV
df_submissao.to_csv("predicoes.csv", index=False)

print("Arquivo 'predicoes.csv' gerado com sucesso!")

#python treinar_ia.py
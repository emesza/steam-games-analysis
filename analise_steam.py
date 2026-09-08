"""
Análise de Dados: Jogos da Steam
---------------------------------
Projeto de portfólio - Matheus Souza

Objetivo: explorar um conjunto de dados de jogos da Steam para responder
perguntas de negócio simples usando Pandas, e gerar gráficos com Matplotlib.

Como rodar:
    pip install pandas matplotlib --break-system-packages
    python analise_steam.py
"""

import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------------------------------------------
# 1. Carregar e inspecionar os dados
# ---------------------------------------------------------------
df = pd.read_csv("steam_games.csv")

print("=" * 60)
print("VISÃO GERAL DO DATASET")
print("=" * 60)
print(f"Total de jogos: {len(df)}")
print(f"Colunas: {list(df.columns)}\n")
print(df.head(), "\n")
print(df.describe(), "\n")

# ---------------------------------------------------------------
# 2. Limpeza básica
# ---------------------------------------------------------------
# Checar valores nulos
print("Valores nulos por coluna:")
print(df.isnull().sum(), "\n")

# Criar uma coluna auxiliar: jogo é gratuito ou pago
df["is_free"] = df["price_usd"] == 0.0

# ---------------------------------------------------------------
# 3. Perguntas de análise
# ---------------------------------------------------------------

# 3.1 Qual gênero aparece com mais frequência?
print("=" * 60)
print("GÊNERO MAIS COMUM")
print("=" * 60)
genre_counts = df["genre"].value_counts()
print(genre_counts, "\n")

# 3.2 Qual o preço médio por gênero (considerando só jogos pagos)?
print("=" * 60)
print("PREÇO MÉDIO POR GÊNERO (apenas jogos pagos)")
print("=" * 60)
avg_price_by_genre = (
    df[~df["is_free"]].groupby("genre")["price_usd"].mean().sort_values(ascending=False)
)
print(avg_price_by_genre.round(2), "\n")

# 3.3 Existe relação entre preço e nota de avaliação positiva?
print("=" * 60)
print("CORRELAÇÃO: PREÇO x % DE AVALIAÇÕES POSITIVAS")
print("=" * 60)
correlation = df["price_usd"].corr(df["positive_review_pct"])
print(f"Coeficiente de correlação: {correlation:.3f}")
print("(perto de 0 = pouca relação linear; perto de 1 ou -1 = relação forte)\n")

# 3.4 Top 10 jogos mais bem avaliados
print("=" * 60)
print("TOP 10 JOGOS MAIS BEM AVALIADOS")
print("=" * 60)
top10 = df.sort_values("positive_review_pct", ascending=False).head(10)
print(top10[["name", "genre", "positive_review_pct"]].to_string(index=False), "\n")

# 3.5 Quantos jogos são gratuitos vs pagos?
print("=" * 60)
print("GRATUITOS x PAGOS")
print("=" * 60)
print(df["is_free"].value_counts().rename({True: "Gratuitos", False: "Pagos"}), "\n")

# 3.6 Tempo médio de jogo por gênero
print("=" * 60)
print("TEMPO MÉDIO DE JOGO (horas) POR GÊNERO")
print("=" * 60)
avg_playtime = df.groupby("genre")["avg_playtime_hours"].mean().sort_values(ascending=False)
print(avg_playtime.round(1), "\n")

# ---------------------------------------------------------------
# 4. Visualizações
# ---------------------------------------------------------------

# Gráfico 1: Quantidade de jogos por gênero
plt.figure(figsize=(9, 5))
genre_counts.plot(kind="bar", color="#2E5395")
plt.title("Quantidade de Jogos por Gênero")
plt.xlabel("Gênero")
plt.ylabel("Número de Jogos")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("grafico_jogos_por_genero.png", dpi=150)
plt.close()
print("Gráfico salvo: grafico_jogos_por_genero.png")

# Gráfico 2: Dispersão preço x avaliação positiva
plt.figure(figsize=(8, 6))
plt.scatter(df["price_usd"], df["positive_review_pct"], alpha=0.6, color="#2E5395")
plt.title("Preço x % de Avaliações Positivas")
plt.xlabel("Preço (USD)")
plt.ylabel("% Avaliações Positivas")
plt.tight_layout()
plt.savefig("grafico_preco_vs_avaliacao.png", dpi=150)
plt.close()
print("Gráfico salvo: grafico_preco_vs_avaliacao.png")

# Gráfico 3: Preço médio por gênero
plt.figure(figsize=(9, 5))
avg_price_by_genre.plot(kind="bar", color="#4C8C4A")
plt.title("Preço Médio por Gênero (jogos pagos)")
plt.xlabel("Gênero")
plt.ylabel("Preço médio (USD)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("grafico_preco_medio_genero.png", dpi=150)
plt.close()
print("Gráfico salvo: grafico_preco_medio_genero.png")

print("\nAnálise concluída! Confira os arquivos .png gerados nesta pasta.")

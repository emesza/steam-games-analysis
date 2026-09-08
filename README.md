# Análise de Dados: Jogos da Steam

Projeto de análise exploratória de dados usando **Python** e **Pandas**, feito para praticar limpeza de dados, agregações e visualização com um tema popular: jogos da plataforma Steam.

## O que o projeto faz

- Carrega um dataset com 62 jogos conhecidos da Steam (gênero, preço, ano de lançamento, % de avaliações positivas, tempo médio de jogo)
- Responde perguntas de análise:
  - Qual gênero é mais comum na base?
  - Qual o preço médio por gênero?
  - Existe correlação entre preço e nota de avaliação?
  - Quais são os 10 jogos mais bem avaliados?
  - Quantos jogos são gratuitos vs pagos?
  - Qual gênero prende mais o jogador (tempo médio de jogo)?
- Gera 3 gráficos (`.png`) com Matplotlib para visualizar os resultados

## Principais descobertas

- **Shooter** é o gênero com mais jogos na base, seguido de Indie e RPG
- Jogos de **Strategy** e **Sports** têm o maior preço médio; **Indie** e **Puzzle**, o menor
- A correlação entre preço e % de avaliações positivas é praticamente nula (≈ -0.06) — preço não é um bom preditor de qualidade percebida
- Jogos de **Simulation**, **Survival** e **Strategy** têm o maior tempo médio de jogo, o que faz sentido dado o caráter de longo prazo desses gêneros

## Como rodar

```bash
pip install pandas matplotlib --break-system-packages
python analise_steam.py
```

## Sobre os dados

Por limitação de escopo (o dataset oficial do Steam tem mais de 80.000 jogos e passa de 100MB), esta versão usa uma amostra compacta e curada com ~60 jogos conhecidos, montada manualmente com dados aproximados de preço e avaliação. A lógica do código é a mesma que se aplicaria ao dataset completo — para escalar, basta trocar o `steam_games.csv` por um dataset maior (ex: [Steam Games Dataset no Kaggle](https://www.kaggle.com/datasets)) mantendo as mesmas colunas.

## Tecnologias usadas

- Python 3
- Pandas
- Matplotlib

---
Projeto feito por Matheus Souza como parte do portfólio de estudos em Ciência de Dados.

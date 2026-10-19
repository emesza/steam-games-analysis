# Análise de Dados: Jogos da Steam

Projeto de análise exploratória de dados usando Python e Pandas, feito para praticar limpeza de dados, agregações e visualização com um tema que faz parte do meu interesse pessoal: jogos, usando dados da plataforma Steam.

## O que o projeto faz

- Carrega um dataset com 62 jogos conhecidos da Steam (gênero, preço, ano de lançamento, % de avaliações positivas, tempo médio de jogo)
- Responde perguntas de análise:
  - Qual gênero é mais comum na base?
  - Qual o preço médio por gênero?
  - Existe correlação entre preço e nota de avaliação?
  - Quais são os 10 jogos mais bem avaliados?
  - Quantos jogos são gratuitos vs pagos?
  - Qual gênero prende mais o jogador (tempo médio de jogo)?
- Gera 3 gráficos (.png) com Matplotlib para visualizar os resultados

## Principais descobertas

- Shooter é o gênero com mais jogos na base, seguido de Indie e RPG
- Jogos de Strategy e Sports têm o maior preço médio; Indie e Puzzle, o menor
- A correlação entre preço e % de avaliações positivas é praticamente nula (≈ -0.06), ou seja, preço não é um bom preditor de qualidade percebida
- Jogos de Simulation, Survival e Strategy têm o maior tempo médio de jogo, o que faz sentido dado o caráter de longo prazo desses gêneros

## Como rodar

```bash
pip install pandas matplotlib --break-system-packages
python analise_steam.py
```

## Sobre os dados

O dataset completo da Steam tem mais de 80 mil jogos e passa de 100MB, então preferi montar uma versão menor com cerca de 60 jogos conhecidos pra focar na lógica da análise sem me perder no tamanho do arquivo. O código funciona do mesmo jeito com uma base maior, é só trocar o `steam_games.csv` por um dataset completo (tem um bom no [Kaggle](https://www.kaggle.com/datasets)) mantendo as mesmas colunas.

## Painel no Power BI

Além da análise em Python, montei um painel interativo no Power BI com os mesmos dados.

![Painel Jogos da Steam](painel_steam.png)

O painel traz cartões-resumo (62 jogos, preço médio de US$ 32,01, 87,19% de avaliações positivas e 118,15 horas de tempo médio de jogo), gráficos por gênero, uma dispersão de preço × avaliação, o top 10 de jogos mais bem avaliados e um filtro por gênero.

Arquivo: [`steam_dashboard.pbix`](steam_dashboard.pbix)

### O que o painel mostra

- Shooter, Indie e RPG são os gêneros com mais jogos na base
- Action, RPG e Strategy têm os maiores preços médios; Shooter, Puzzle e Indie, os menores. Parte disso se explica pelos jogos gratuitos, que puxam a média de Shooter para baixo
- Puzzle, Indie e RPG têm as melhores avaliações médias; Sports tem a menor
- Simulation, Survival e Strategy concentram o maior tempo médio de jogo
- Na dispersão, não há relação clara entre preço e avaliação: há jogos bem avaliados em todas as faixas de preço

### Ajuste de dados feito no Power BI

Ao importar o CSV, os preços apareceram multiplicados por 100 (por exemplo, 29.99 virou 2999), porque o Power BI em português lê o ponto como separador de milhar. Corrigi definindo o tipo da coluna `price_usd` como número decimal com a localidade Inglês (Estados Unidos).

## Tecnologias usadas

- Python 3
- Pandas
- Matplotlib

---
Projeto feito por Matheus Souza como parte do portfólio de estudos.

# Estrutura do Projeto de Classificação

Este documento descreve a estrutura de diretórios criada para o projeto de classificação de churn.

**Origem dos dados:** [Kaggle - Churn Modelling Dataset](https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling)

- data/
  - analysis/: gráficos e .csv resultantes da análise de dados
  - processed/: datasets prontos para modelagem
- notebooks/: análises exploratórias e protótipos
- src/
  - models/: treino, avaliação e persistência de modelos
  - pipelines/: orquestração de passos de ML (treino/inferência)
- scripts/: scripts de linha de comando (treino, previsão)
- docs/: documentação adicional

# Estrutura do Projeto de Classificação

Este documento descreve a estrutura de diretórios criada para o projeto de classificação de churn.

**Origem dos dados:** [Kaggle - Churn Modelling Dataset](https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling)

- data/
  - analysis/: arquivos temporários referente a gráficos e .csv resultantes da análise de dados
  - processed/: arquivos temporários referente a tratamento de dados, treinamento e otimização de modelos
- notebooks/: análises exploratórias e protótipos
- src/
  - analysis/: análise de dados
  - models/: treino, avaliação e persistência de modelos
  - preprocessing/: pré-processamento de dados
  - pipelines/: orquestração de passos de ML (treino/inferência)
  - tracking/: scripts de criação dos artefatos do MLFlow
- docs/: documentação adicional

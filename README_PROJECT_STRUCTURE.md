# Estrutura do Projeto de Classificação

Este documento descreve a estrutura de diretórios criada para o projeto de classificação de churn.

- data/
  - raw/: dados brutos
  - interim/: dados intermediários (limpeza, imputação)
  - processed/: datasets prontos para modelagem
- notebooks/: análises exploratórias e protótipos
- src/
  - data/: carregamento, validação e transformação inicial de dados
  - features/: engenharia de atributos e seleção de variáveis
  - models/: treino, avaliação e persistência de modelos
  - pipelines/: orquestração de passos de ML (treino/inferência)
- models/: artefatos de modelos treinados (salvos)
- reports/
  - figures/: gráficos gerados
  - metrics/: relatórios e métricas
- scripts/: scripts de linha de comando (treino, previsão)
- docs/: documentação adicional


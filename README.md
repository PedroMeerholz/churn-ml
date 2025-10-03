# Documentação do Projeto: Modelo Preditivo de Churn Bancário

## Sumário

- [Visão Geral](#visão-geral)
- [Problema de Negócio](#problema-de-negócio)
- [Objetivo](#objetivo)
- [Solução Proposta](#solução-proposta)
- [Métricas de Sucesso](#métricas-de-sucesso)
- [Público-Alvo](#público-alvo)
- [Arquitetura e MLOps](#arquitetura-e-mlops)
- [Contato](#contato)

---

## Visão Geral

A perda de clientes (churn) é um desafio comum em mercados financeiros competitivos. Diante disso, este projeto busca apoiar uma instituição bancária na redução do churn, reconhecendo que a retenção de clientes é mais econômica do que a aquisição de novos, o que torna essencial a identificação antecipada de clientes insatisfeitos ou propensos a encerrar suas contas.

---

## Problema de Negócio

A saída de cada cliente resulta em:

- **Perda de Receita:** Clientes levam saldos, investimentos e oportunidades futuras.
- **Oportunidades Perdidas:** Falta de atuação nos estágios iniciais da insatisfação.
- **Ineficiência de Custos:** Campanhas genéricas desperdiçam recursos em clientes de baixo risco.

---

## Objetivo

Desenvolver e implantar um sistema de Machine Learning que, a partir dos dados dos clientes, seja capaz de prever com precisão a probabilidade de cada cliente realizar churn, permitindo à instituição bancária agir proativamente na retenção.

---

## Solução Proposta

O sistema será baseado em um modelo de classificação binária, capaz de distinguir entre clientes propensos e não propensos ao churn. Para isso, serão utilizados dados históricos dos clientes, abrangendo informações demográficas, produtos contratados e comportamento transacional. Além disso, o sistema contará com uma interface interativa, permitindo que usuários consultem e utilizem o modelo de forma prática e intuitiva.

---

## Métricas de Sucesso

### Métricas de Negócio

- Redução da taxa de churn trimestral em X%

### Métricas do Modelo

- **Recall (Sensibilidade):** Prioridade alta para identificar o máximo de clientes que realmente darão churn.
- **Precision:** Minimizar falsos positivos para otimizar recursos da equipe de retenção.
- **F1-Score:** Equilíbrio entre precision e recall.
- **AUC-ROC:** Avaliação da capacidade discriminatória do modelo.

---

## Público-Alvo

A solução é destinada principalmente às equipes de **Retenção** e **Marketing**, que utilizarão as pontuações de risco para segmentar clientes e direcionar ações como:

- Ofertas especiais
- Contato proativo de gerentes de conta
- Pesquisas de satisfação
## Treinamento e Otimização dos Modelos
> **Observação:**  
> Todos os resultados apresentados nesta seção referem-se à execução realizada no notebook `notebooks/tuning.ipynb`. Assim, as métricas e avaliações reproduzem exatamente o que foi obtido neste arquivo, podendo variar caso novos treinamentos ou atualizações sejam feitos no futuro.


### 1️⃣ Treinamento Inicial (Baseline)

- **Contexto:**  
  Após os testes de feature engineering, utilizei os dados no formato final do Teste 4 para treinar diferentes modelos sem otimização de hiperparâmetros.  
  Abaixo estão as principais métricas de desempenho de cada modelo avaliado.

---

#### **a) Random Forest Classifier**

- **Métricas:**
  - Classe 0: precisão = 0.9254, revocação = 0.7789, f1-score = 0.8458, suporte = 1194
  - Classe 1: precisão = 0.4667, revocação = 0.7549, f1-score = 0.5768, suporte = 306
  - **Acurácia geral:** 0.7740 (total de 1500 amostras)

- **Matriz de confusão:**
  - Real 0, Prev 0: 930 | Real 0, Prev 1: 264
  - Real 1, Prev 0: 75  | Real 1, Prev 1: 231

---

#### **b) Gradient Boosting**

- **Métricas:**
  - Classe 0: precisão = 0.9302, revocação = 0.7814, f1-score = 0.8493, suporte = 1194
  - Classe 1: precisão = 0.4748, revocação = 0.7712, f1-score = 0.5878, suporte = 306
  - **Acurácia geral:** 0.7793

- **Matriz de confusão:**
  - Real 0, Prev 0: 933 | Real 0, Prev 1: 261
  - Real 1, Prev 0: 70  | Real 1, Prev 1: 236

---

#### **c) AdaBoost**

- **Métricas:**
  - Classe 0: precisão = 0.9156, revocação = 0.7814, f1-score = 0.8432, suporte = 1194
  - Classe 1: precisão = 0.4574, revocação = 0.7190, f1-score = 0.5591, suporte = 306
  - **Acurácia geral:** 0.7687

- **Matriz de confusão:**
  - Real 0, Prev 0: 933 | Real 0, Prev 1: 261
  - Real 1, Prev 0: 86  | Real 1, Prev 1: 220

---

#### **d) Bagging**

- **Métricas:**
  - Classe 0: precisão = 0.9159, revocação = 0.7839, f1-score = 0.8448, suporte = 1194
  - Classe 1: precisão = 0.4603, revocação = 0.7190, f1-score = 0.5612, suporte = 306
  - **Acurácia geral:** 0.7707

- **Matriz de confusão:**
  - Real 0, Prev 0: 936 | Real 0, Prev 1: 258
  - Real 1, Prev 0: 86  | Real 1, Prev 1: 220

---

#### **e) Extra Trees**

- **Métricas:**
  - Classe 0: precisão = 0.9196, revocação = 0.7755, f1-score = 0.8414, suporte = 1194
  - Classe 1: precisão = 0.4564, revocação = 0.7353, f1-score = 0.5632, suporte = 306
  - **Acurácia geral:** 0.7673

- **Matriz de confusão:**
  - Real 0, Prev 0: 926 | Real 0, Prev 1: 268
  - Real 1, Prev 0: 81  | Real 1, Prev 1: 225

---

#### **f) XGBoost**

- **Métricas:**
  - Classe 0: precisão = 0.9183, revocação = 0.7630, f1-score = 0.8335, suporte = 1194
  - Classe 1: precisão = 0.4429, revocação = 0.7353, f1-score = 0.5528, suporte = 306
  - **Acurácia geral:** 0.7573

- **Matriz de confusão:**
  - Real 0, Prev 0: 911 | Real 0, Prev 1: 283
  - Real 1, Prev 0: 81  | Real 1, Prev 1: 225

---

#### **g) LightGBM**

- **Métricas:**
  - Classe 0: precisão = 0.9224, revocação = 0.7663, f1-score = 0.8371, suporte = 1194
  - Classe 1: precisão = 0.4508, revocação = 0.7484, f1-score = 0.5627, suporte = 306
  - **Acurácia geral:** 0.7627

- **Matriz de confusão:**
  - Real 0, Prev 0: 915 | Real 0, Prev 1: 279
  - Real 1, Prev 0: 77  | Real 1, Prev 1: 229

---

### 2️⃣ Otimização de Hiperparâmetros 

- **Metodologia:**  
  Otimizei os principais modelos utilizando o Optuna, com a métrica alvo sendo o `F1 Score`.

- **Resultado:**  
  - Mesmo após otimização, os modelos não superaram os respectivos baselines.
  - [Resultados detalhados da otimização podem ser incluídos posteriormente.]

---

### 3️⃣ Análise de Custos dos Erros dos Modelos

- **Cenário de Negócio:**  
  Para avaliar o impacto financeiro dos erros de previsão, atribuí custos hipotéticos aos tipos de erro:

  - **Falso Positivo (prevê churn, mas o cliente não sairia):** R$ 230,00  
    _Custo da ação de retenção desnecessária._
  - **Falso Negativo (não prevê churn, mas o cliente sai):** R$ 791,40  
    _Perda do lucro médio de R$ 65,95/mês × 12 meses._

- **Cálculo do custo total:**  
  Multiplicam-se os totais de falsos positivos e falsos negativos (segundo cada matriz de confusão) pelos respectivos valores acima.

#### Tabela – Custo dos Erros por Modelo

| Colocação | Modelo                         | Custo dos Erros     |
|-----------|-------------------------------|----------------------|
| 1         | Baseline_Gradient Boosting     | R$ 115.428,00       |
| 2         | Baseline_Random Forest         | R$ 120.075,00       |
| 3         | Baseline_LightGBM              | R$ 125.107,80       |
| 4         | Baseline_Extra Trees           | R$ 125.743,40       |
| 5         | Baseline_Bagging               | R$ 127.400,40       |
| 6         | Baseline_AdaBoost              | R$ 128.090,40       |
| 7         | Baseline_XGBoost               | R$ 129.193,40       |
| 8         | Optmized_Gradient Boosting     | R$ 131.562,80       |
| 9         | Optmized_XGBoost               | R$ 140.654,00       |
| 10        | Optmized_Random Forest         | R$ 141.749,60       |
| 11        | Optmized_LightGBM              | R$ 142.081,00       |
| 12        | Optmized_AdaBoost              | R$ 142.466,80       |
| 13        | Optmized_Bagging               | R$ 143.129,60       |
| 14        | Optmized_Extra Trees           | R$ 148.919,20       |

---

### 4️⃣ Economia Potencial ao Negócio

- **Cenário Sem Modelo:**  
  Num cenário onde nenhuma ação é tomada, 2037 clientes deram churn, totalizando um custo de R$ 1.612.081,80 (2037 × R$ 791,40).

- **Redução proporcionada:**  
  O melhor modelo (Gradient Boosting - baseline) reduz o custo para R$ 115.428,00, representando uma economia de R$ 1.496.653,80, ou seja, redução de 92,83% nas perdas com churn.

---

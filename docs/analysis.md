# Análise de Dados

Para iniciar a análise de dados, verifiquei algumas informações básicas:
- Número de dados nulos
- Número de linhas duplicadas
- Colunas disponíveis
- Linhas iniciais do dataset

A partir dessas observações, elaborei perguntas que poderiam ser respondidas por meio de estatísticas descritivas e inferenciais, direcionando a análise. Abaixo, apresento as perguntas e os métodos utilizados para respondê-las.

## 🟦 Categoria 1: Análise Demográfica

### 1️⃣ Algum gênero tem uma maior tendência a cancelar os serviços?
- **Método:** Gráfico de Colunas  
- **Resultado:** _(Colocar gráfico aqui)_

---

### 2️⃣ A diferença de churns entre os gêneros é significativa?
- **Método:** Teste Qui-Quadrado  
- **Hipóteses:**
  - **H0:** Não existe associação entre Gênero e Churn
  - **H1:** Existe associação entre Gênero e Churn
- **Resultado:**  
  - statistics: `112.918571`  
  - p-value: `2.248210e-26`  
  - **Interpretação:** Com alpha = 0.05, rejeitamos H0.

---

### 3️⃣ Alguma faixa de idade tem uma maior tendência a cancelar os serviços?
- **Método:** Gráfico Boxplot e Histograma  
- **Resultado:** _(Colocar gráfico aqui)_

---

### 4️⃣ A diferença de churns entre as faixas etárias é significativa?
- **Método:** Teste T  
- **Hipóteses:**
  - **H0:** Não existe diferença significativa entre as médias de idade dos clientes que deram e que não deram churn
  - **H1:** Existe diferença significativa entre as médias de idade dos clientes que deram e que não deram churn
- **Resultado:**  
  - statistics: `-29.766815`  
  - p-value: `1.239931e-186`  
  - **Interpretação:** Com alpha = 0.05, rejeitamos H0.

---

## 🟩 Categoria 2: Análise Geográfica e de Produto

### 1️⃣ Qual região possui mais churn?
- **Método:** Gráfico de Colunas  
- **Resultado:** _(Colocar gráfico aqui)_

---

### 2️⃣ A diferença de churns entre as regiões é significativa?
- **Método:** Teste Qui-Quadrado  
- **Hipóteses:**
  - **H0:** Não existe associação entre Localização e Churn
  - **H1:** Existe associação entre Localização e Churn
- **Resultado:**  
  - statistics: `301.255337`  
  - p-value: `3.830318e-66`  
  - **Interpretação:** Com alpha = 0.05, rejeitamos H0.

---

### 3️⃣ Os clientes que deram churn possuíam cartão de crédito?
- **Método:** Gráfico de Colunas  
- **Resultado:** _(Colocar gráfico aqui)_

---

### 4️⃣ A diferença de churns entre clientes que tinham ou não cartão de crédito é significativa?
- **Método:** Teste Qui-Quadrado  
- **Hipóteses:**
  - **H0:** Não existe associação entre ter cartão de crédito e churn
  - **H1:** Existe associação entre ter cartão de crédito e churn
- **Resultado:**  
  - statistics: `0.471338`  
  - p-value: `0.492372`  
  - **Interpretação:** Com alpha = 0.05, falhamos em rejeitar h0.

---

## 🟨 Categoria 3: Análise Comportamental e de Uso

### 1️⃣ Os clientes que deram churn tinham quanto tempo de contrato, em média? A diferença é significativa?
- **Método:** Média e Teste T  
- **Médias:**
  - Churn: `4.93`
  - Não churn: `5.03`
- **Hipóteses:**
  - **H0:** Não existe diferença significativa entre as médias de tempo de contrato
  - **H1:** Existe diferença significativa entre as médias de tempo de contrato
- **Resultado:**  
  - statistics: `1.400058`  
  - p-value: `0.161527`  
  - **Interpretação:** Com alpha = 0.05, falhamos em rejeitar h0.

---

### 2️⃣ Os clientes que deram churn tinham um bom score de crédito?
- **Método:** Boxplot e Histograma  
- **Resultado:** _(Colocar gráficos aqui)_
- **Hipóteses:**
  - **H0:** Não existe diferença significativa entre as médias de score
  - **H1:** Existe diferença significativa entre as médias de score
- **Resultado:**  
  - statistics: `2.710078`  
  - p-value: `0.006738`  
  - **Interpretação:** Com alpha = 0.05, rejeitamos H0.

---

### 3️⃣ A média do score de clientes que deram ou não churn possui diferença significativa?
- **Método:** Teste T  
- **Hipóteses:**
  - **H0:** Não existe diferença significativa entre as médias de score
  - **H1:** Existe diferença significativa entre as médias de score
- **Resultado:**  
  - statistics: `2.710078`  
  - p-value: `0.006738`  
  - **Interpretação:** Com alpha = 0.05, rejeitamos H0.

---

### 4️⃣ Qual a média de serviços contratados por clientes que deram ou não churn?
- **Método:** Média  
- **Médias:**
  - Churn: `1.475209`
  - Não churn: `1.544267`
- **Hipóteses:**
  - **H0:** Não existe diferença significativa entre as médias de serviços contratados
  - **H1:** Existe diferença significativa entre as médias de serviços contratados
- **Resultado:**  
  - statistics: `1.400058`  
  - p-value: `0.161527`  
  - **Interpretação:** Com alpha = 0.05, falhamos em rejeitar h0.

---

### 5️⃣ A média de serviços contratados entre clientes que deram ou não churn possui diferença significativa?
- **Método:** Teste T  
- **Hipóteses:**
  - **H0:** Não existe diferença significativa entre as médias de serviços contratados
  - **H1:** Existe diferença significativa entre as médias de serviços contratados
- **Resultado:**  
  - statistics: `4.786985`  
  - p-value: `0.000002`  
  - **Interpretação:** Com alpha = 0.05, rejeitamos H0.

---

## 🟥 Categoria 4: Qualidade dos Dados

### 1️⃣ Os dados possuem outliers?
- **Método:** Gráfico Boxplot  
- **Resultado:** _(Colocar gráfico aqui)_

---

### 2️⃣ O conjunto de dados é balanceado? Qual a proporção das classes?
- **Método:** Contagem de Valores  
- **Resultado:**
  - Proporção de clientes que **não deram churn**: `79.63%`
  - Proporção de clientes que **deram churn**: `20.37%`

---

### 3️⃣ Existe alguma relação linear entre as features?
- **Método:** Pairplot
- **Resultado:** _(Colocar gráfico aqui)_

---
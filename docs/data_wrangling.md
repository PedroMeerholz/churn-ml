# 🟦 Pré-processamento de Dados e Feature Engineering

### 1️⃣ Considerações Iniciais
- O dataset **não possui dados nulos ou duplicatas**
- Os resultados dos testes de hipóteses são **indicativos, mas não conclusivos**
- O dataset está **desbalanceado**
- **Nem todas as colunas serão necessárias**
- As colunas **Geography** e **Gender** precisarão ser codificadas

---

### 2️⃣ Possíveis Estratégias Futuras

Os primeiros testes com modelos serão realizados utilizando os dados em sua forma mais original possível, com o mínimo de transformações. Isso permitirá avaliar o desempenho base dos algoritmos e identificar quais melhorias realmente agregam valor ao processo de modelagem. Após essa etapa inicial, as estratégias abaixo serão implementadas para buscar ganhos de performance e robustez nos modelos:

- **Padronização e normalização** dos dados
- **Criação de novas features** com base em: `Tenure`, `Age`, `CreditScore`

---

### 3️⃣ Remoção de Colunas

- **Colunas removidas:**  
  - `RowNumber`  
  - `CustomerId`  
  - `Surname`  

- **Justificativas:**  
  - `RowNumber` e `CustomerId`: representam valores únicos (não agregam informação preditiva)
  - `Surname`: possui pouca variação de valores relevantes

---

### 4️⃣ Codificação de Colunas Categóricas

- **Colunas a serem codificadas:**  
  - `Geography`  
  - `Gender`  

- **Valores para `Geography`:**
  - France: `0`
  - Spain: `1`
  - Germany: `2`

- **Valores para `Gender`:**
  - Female: `0`
  - Male: `1`

---
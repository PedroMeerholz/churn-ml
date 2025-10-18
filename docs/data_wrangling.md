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

# Testes

O primeiro teste foi criar um modelo baseline, utilizando o RandomForest e verificar como o modelo iria se comportar com os dados que tinha pouca preparação. As principais métricas a serem analisada são recall e precision. Separando 80% para treino e 20% para teste, esses foram os resultados:

**Relatório de Classificação:**

| Classe   | Precision | Recall | F1-score | Samples |
|----------|-----------|--------|----------|---------|
| 0        | 0.88      | 0.96   | 0.92     |   1593  |
| 1        | 0.77      | 0.47   | 0.58     |   407   |

**Acurácia do modelo:** 0.86 (86%)

Outra informação importante coletada, foi a de **Feature Importance**, que teve estes resultados:

| Feature         | Importance |
|-----------------|------------|
| Age             | 0.235319   |
| EstimatedSalary | 0.147366   |
| CreditScore     | 0.143241   |
| Balance         | 0.142890   |
| NumOfProducts   | 0.131191   |
| Tenure          | 0.079106   |
| Geography       | 0.042938   |
| IsActiveMember  | 0.040365   |
| Gender          | 0.019279   |
| HasCrCard       | 0.018303   |

Como é possível observar, os testes de hipótese feitos com Tempo de Contrato (Tenure) e Cartão de Crédito (HasCrCard), indicam algo verdadeiro, pois a importância destas duas features para o modelo, é baixa. O que não ocorre em relação ao teste de hipótese da Quantidade de Produtos Contratados (NumOfProducts).

Testes de Feature Engineering Realizados:

1. **Remoção das colunas HasCrCard e Tenure:**  
   Eliminei as colunas relacionadas à posse de cartão de crédito e tempo de contrato, já que apresentaram baixa importância na análise de Feature Importance. Essa remoção resultou em uma leve piora no desempenho do modelo, especificamente uma redução de 1% no recall para a classe 1 (clientes que deram churn).

2. **Remoção das colunas com menos de 10% de importância:**  
   Excluí todas as variáveis cuja importância era inferior a 10% de acordo com a análise anterior. O impacto foi uma diminuição de 6% no recall da classe 1, indicando que algumas dessas variáveis, apesar da baixa importância individual, colaboravam para o desempenho do modelo em identificar churns.

3. **Remoção das colunas com menos de 10% de importância e criação de faixas para Age e CreditScore:**  
   Além de eliminar as colunas de pouca importância, categorizei as variáveis “Age” e “CreditScore” em grupos. Essa transformação resultou numa redução de 7% no recall da classe 1, sugerindo que a criação de categorias não compensou a perda de informação das variáveis removidas.

4. **Balanceamento das classes:**  
   Apliquei técnicas de balanceamento para igualar a proporção das classes. Ainda que o recall da classe 1 tenha subido expressivamente (+30%), houve uma queda significativa de 18% no recall da classe 0 (clientes que não deram churn), mostrando um trade-off comum em situações de desbalanceamento.

5. **Remoção das colunas com menos de 10% de importância juntamente com balanceamento das classes:**  
   Combinei a exclusão das variáveis menos importantes com o balanceamento das classes. Nessa configuração, o recall de clientes sem churn caiu ainda mais (redução de 22%), enquanto o recall dos clientes que deram churn aumentou 25%.

6. **Criação de faixas para Tenure, Age e CreditScore + Balanceamento das classes:**  
   Categorizei as variáveis “Tenure”, “Age” e “CreditScore”, além de balancear as classes. Novamente, obtive aumentos consideráveis no recall da classe 1 (+30%), com redução de 18% no recall da classe 0.

7. **Novas features (proporção entre produtos contratados e tempo de contrato) + todas transformações anteriores:**  
   Além das categorizações e balanceamento, criei uma nova feature representando a razão entre número de serviços contratados e o tempo de contrato. O impacto foi semelhante ao teste anterior: recall da classe 1 aumentou 30% e recall da classe 0 diminuiu 19%.

8. **Todas as transformações do Teste 7 + normalização dos dados:**  
   Por fim, após aplicar todas as transformações do teste 7, normalizei os dados numéricos. Não houve variação adicional significativa: a redução no recall da classe 0 se manteve em 19% e o aumento no recall da classe 1 em 30%.

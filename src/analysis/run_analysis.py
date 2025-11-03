import os
import mlflow
import numpy as np
import pandas as pd
import seaborn as sns
from scipy import stats
import matplotlib.pyplot as plt

from tracking.artifact_generation import save_artifact

from dotenv import load_dotenv
load_dotenv()


def countplot(title, data, x, hue, artifact_path):
    plt.figure(figsize=(10, 5))
    plt.title(title)
    sns.countplot(data=data, x=x, hue=hue)
    plt.ylabel('Quantidade de churns')
    plt.savefig(artifact_path)
    plt.close()


def plot_box_hist(df, suptitle, column, artifact_path):
    fig, axes = plt.subplots(1, 2, figsize=(16, 5))
    fig.suptitle(suptitle)

    sns.boxplot(data=df, x='Exited', y=column, ax=axes[0])
    axes[0].set_title('Boxplot')

    sns.histplot(data=df, x=column, hue='Exited', ax=axes[1])
    axes[1].set_title('Histograma')

    plt.tight_layout()
    plt.savefig(artifact_path)
    plt.close()


def chi2(data, column, artifact_path, alpha=0.05):
    crosstab = pd.crosstab(data[column], data['Exited'])
    chi_scores = stats.chi2_contingency(crosstab)
    chi2 = chi_scores[0]
    pvalue = chi_scores[1]

    chi2_df = {'Qui2': [chi2], 'p-value': [pvalue], 'hypotesis': 'H1' if pvalue < alpha else 'H0'}
    chi2_df = pd.DataFrame(chi2_df)
    chi2_df.index = [column]
    chi2_df.to_csv(artifact_path, index=False)


def t_test(data, column, artifact_path, alpha=0.05):
    no_churn = data[data['Exited'] == 0][column]
    churn = data[data['Exited'] == 1][column]

    ttest_scores = stats.ttest_ind(no_churn, churn)
    statistics = ttest_scores[0]
    pvalue = ttest_scores[1]

    ttest_df = {'statistics': [statistics], 'p-value': [pvalue], 'hypotesis': 'H1' if pvalue < alpha else 'H0'}
    ttest_df = pd.DataFrame(ttest_df)
    ttest_df.index = [column]
    ttest_df.to_csv(artifact_path, index=False)


def run_analysis(df):
    analysis_artifact_path = os.environ['ANALYSIS_ARTIFACT_PATH'] 
    
    with mlflow.start_run(run_name="Análise de Dados", nested=True) as run:
        basic_info = {
            'Número de linhas': [df.shape[0]],
            'Número de colunas': [df.shape[1]],
            'Número de linhas duplicadas': [df.duplicated().sum()],
            'Número de nulos': [df.isna().sum().sum()]
        }
        basic_info = pd.DataFrame(data=basic_info)
        local_path = os.path.join(analysis_artifact_path, 'informacoes_basicas.csv')
        basic_info.to_csv(local_path, index=False)
        # mlflow.log_artifact(local_path)
        # os.remove(local_path)
        save_artifact(local_path=local_path)

        sample = df.head()
        local_path = os.path.join(analysis_artifact_path, 'head.csv')
        sample.to_csv(local_path, index=False)
        # mlflow.log_artifact(local_path)
        # os.remove(local_path)
        save_artifact(local_path=local_path)

        df.drop(['RowNumber'], axis=1, inplace=True)

        # Categoria 1: Análise Demográfica
        artifact_path = 'analise_demografica'
        demographic_analysis_dir_path = os.path.join(analysis_artifact_path, artifact_path)
        
        # Pergunta 1: Algum gênero tem uma maior tendência a cancelar os serviços?
        local_path = os.path.join(demographic_analysis_dir_path, 'churn_by_gender.png')
        countplot('Quantidade de churns por gênero', df, 'Gender', 'Exited', local_path)
        # mlflow.log_artifact(local_path=local_path, artifact_path=artifact_path)
        # os.remove(local_path)
        save_artifact(local_path=local_path, artifact_path=artifact_path)

        # Pergunta 2: A diferença de churns entre os gêneros, é significativa?
        local_path = os.path.join(demographic_analysis_dir_path, 'gender_chi2.csv')
        chi2(df, 'Gender', local_path)
        # mlflow.log_artifact(local_path=local_path, artifact_path=artifact_path)
        # os.remove(local_path)
        save_artifact(local_path=local_path, artifact_path=artifact_path)

        # Pergunta 3: Alguma faixa de idade tem uma maior tendência a cancelar os serviços?
        local_path = os.path.join(demographic_analysis_dir_path, 'age_distribution.png')
        plot_box_hist(df, 'Diferença de Distribuição de Idades Entre Churn e Não Churn', 'Age', local_path)
        # mlflow.log_artifact(local_path=local_path, artifact_path=artifact_path)
        # os.remove(local_path)
        save_artifact(local_path=local_path, artifact_path=artifact_path)

        # Pergunta 4: A diferença de churns entre as faixas etárias, é significativa?
        local_path = os.path.join(demographic_analysis_dir_path, 'age_ttest.csv')
        t_test(df, 'Age', local_path)
        # mlflow.log_artifact(local_path=local_path, artifact_path=artifact_path)
        # os.remove(local_path)
        save_artifact(local_path=local_path, artifact_path=artifact_path)

        # Categoria 2: Análise Geográfica e de Produto
        artifact_path = 'analise_geografica_e_de_produto'
        geographic_and_product_dir_path = os.path.join(analysis_artifact_path, artifact_path)

        # Pergunta 1: Qual região possui mais churn
        local_path = os.path.join(geographic_and_product_dir_path, 'churn_by_location.png')
        countplot('Quantidade de churns por localização', df, 'Geography', 'Exited', local_path)
        # mlflow.log_artifact(local_path=local_path, artifact_path=artifact_path)
        # os.remove(local_path)
        save_artifact(local_path=local_path, artifact_path=artifact_path)

        # Pergunta 2: A diferença de churns entre as regiões, é significativa?
        local_path = os.path.join(geographic_and_product_dir_path, 'geography_chi2.csv')
        chi2(df, 'Geography', local_path, alpha=0.05)
        # mlflow.log_artifact(local_path=local_path, artifact_path=artifact_path)
        # os.remove(local_path)
        save_artifact(local_path=local_path, artifact_path=artifact_path)

        # Pergunta 3: Os clientes que deram churn possuiam cartão de crédito?
        local_path = os.path.join(geographic_and_product_dir_path, 'churn_by_credit_card.png')
        countplot('Quantidade de churns entre clientes com ou sem cartão de crédito', df, 'HasCrCard', 'Exited', local_path)
        # mlflow.log_artifact(local_path=local_path, artifact_path=artifact_path)
        # os.remove(local_path)
        save_artifact(local_path=local_path, artifact_path=artifact_path)

        # Pergunta 4: A diferença de churns entre clientes que tinham ou não cartão de crédito, é significativa?
        local_path = os.path.join(geographic_and_product_dir_path, 'credit_card_ttest.csv')
        chi2(df, 'HasCrCard', local_path, alpha=0.05)
        # mlflow.log_artifact(local_path=local_path, artifact_path=artifact_path)
        # os.remove(local_path)
        save_artifact(local_path=local_path, artifact_path=artifact_path)

        # Categoria 3: Análise Comportamental e de Uso
        artifact_path = 'analise_comportamental'
        behavioral_dir_path = os.path.join(analysis_artifact_path, artifact_path)

        no_churn_df = df[df['Exited'] == 0]
        no_churn_df = no_churn_df.drop('CustomerId', axis=1)

        churn_df = df[df['Exited'] == 1]
        churn_df = churn_df.drop('CustomerId', axis=1)

        # Pergunta 1: Os clientes que deram churn tinham quanto tempo de contrato, em média? A diferença é significativa?
        local_path = os.path.join(behavioral_dir_path, 'mean_tenure.csv')
        churn_customer_average_tenure = churn_df['Tenure'].mean()
        no_churn_customer_average_tenure = no_churn_df['Tenure'].mean()
        average_tenure_df = pd.DataFrame({
            'Churn': [churn_customer_average_tenure],
            'No Churn': [no_churn_customer_average_tenure]
        })
        average_tenure_df.to_csv(local_path)
        # mlflow.log_artifact(local_path=local_path, artifact_path=artifact_path)
        # os.remove(local_path)
        save_artifact(local_path=local_path, artifact_path=artifact_path)

        local_path = os.path.join(behavioral_dir_path, 'tenure_ttest.csv')
        t_test(df, 'Tenure', local_path)
        # mlflow.log_artifact(local_path=local_path, artifact_path=artifact_path)
        # os.remove(local_path)
        save_artifact(local_path=local_path, artifact_path=artifact_path)

        # Pergunta 2: Os clientes que deram churn tinham um bom score de crédito?
        local_path = os.path.join(behavioral_dir_path, 'score_distribution.png')
        plot_box_hist(df, 'Diferença de Distribuição de Score Entre Churn e Não Churn', 'CreditScore', local_path)
        # mlflow.log_artifact(local_path=local_path, artifact_path=artifact_path)
        # os.remove(local_path)
        save_artifact(local_path=local_path, artifact_path=artifact_path)

        # Pergunta 3: A média do score de clientes que deram ou não churn, possui diferença significativa?
        local_path = os.path.join(behavioral_dir_path, 'score_ttest.csv')
        t_test(df, 'CreditScore', local_path)
        # mlflow.log_artifact(local_path=local_path, artifact_path=artifact_path)
        # os.remove(local_path)
        save_artifact(local_path=local_path, artifact_path=artifact_path)

        # Pergunta 4: Os clientes que deram churn haviam contratado quantos serviços, em média?
        local_path = os.path.join(behavioral_dir_path, 'mean_product_number.csv')
        churn_customer_average_services = churn_df['NumOfProducts'].mean()
        no_churn_customer_average_services = no_churn_df['NumOfProducts'].mean()
        average_product_number_df = pd.DataFrame({
            'Churn': [churn_customer_average_services],
            'No Churn': [no_churn_customer_average_services]
        })
        average_product_number_df.to_csv(local_path)
        # mlflow.log_artifact(local_path=local_path, artifact_path=artifact_path)
        # os.remove(local_path)
        save_artifact(local_path=local_path, artifact_path=artifact_path)

        # Pergunta 5: A média de serviços contratados entre clientes que deram ou não churn, possui diferença significativa?
        local_path = os.path.join(behavioral_dir_path, 'product_number_ttest.csv')
        t_test(df, 'NumOfProducts', local_path)
        # mlflow.log_artifact(local_path=local_path, artifact_path=artifact_path)
        # os.remove(local_path)
        save_artifact(local_path=local_path, artifact_path=artifact_path)

        # Categoria 4: Qualidade dos Dados
        artifact_path = 'qualidade_dos_dados'
        data_quality_dir_path = os.path.join(analysis_artifact_path, artifact_path)

        # Pergunta 1: Os dados dos clientes que não deram churn, possuem outliers?
        local_path = os.path.join(data_quality_dir_path, 'outliers.png')
        columns = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'EstimatedSalary']
        n_cols = 2
        n_rows = int(np.ceil(len(columns) / n_cols))
        fig, axes = plt.subplots(n_rows, n_cols, figsize=(16, 12))
        axes = axes.flatten()
        fig.suptitle('Boxplot Comparativo entre Churn e Não Churn')

        for i, col in enumerate(columns):
            sns.boxplot(data=df, x=col, y='Exited', orient='h', ax=axes[i], hue='Exited')
            axes[i].set_title(col)
            axes[i].set_ylabel('Exited')
            axes[i].set_xlabel(col)
            axes[i].legend(title='Exited', loc='best')

        for j in range(i+1, len(axes)):
            fig.delaxes(axes[j])

        plt.savefig(local_path)
        plt.tight_layout(rect=[0, 0.03, 1, 0.97])
        # mlflow.log_artifact(local_path=local_path, artifact_path=artifact_path)
        # os.remove(local_path)
        save_artifact(local_path=local_path, artifact_path=artifact_path)

        # Pergunta 2: O conjunto de dados é balanceado? Qual a proporção das classes?
        class_proportion = df['Exited'].value_counts(normalize=True)
        local_path = os.path.join(data_quality_dir_path, 'class_proportion.csv')
        class_proportion.to_csv(local_path, index=True)
        # mlflow.log_artifact(local_path=local_path, artifact_path=artifact_path)
        # os.remove(local_path)
        save_artifact(local_path=local_path, artifact_path=artifact_path)

        # Pergunta 3: Existe alguma relação linear entre as features?
        local_path = os.path.join(data_quality_dir_path, 'pairplot.png')
        sns.pairplot(df, hue='Exited')
        plt.savefig(local_path)
        # mlflow.log_artifact(local_path=local_path, artifact_path=artifact_path)
        # os.remove(local_path)
        save_artifact(local_path=local_path, artifact_path=artifact_path)

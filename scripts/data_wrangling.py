import pandas as pd

import mlflow
mlflow.set_tracking_uri('http://localhost:5000')
mlflow.set_experiment('Pré-processamento de Dados')

import os
from dotenv import load_dotenv
load_dotenv()


df = pd.read_csv('https://pedromeerholz-churn-ml.s3.sa-east-1.amazonaws.com/Churn_Modelling.csv')


with mlflow.start_run():
    data_wrangling_artifact_path = os.environ['DATA_WRANGLING_ARTIFACT_PATH']
    
    # Remoção de Colunas
    df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

    # Colunas Categóricas
    geography_encoder = {country: idx for idx, country in enumerate(df['Geography'].unique())}
    df['Geography'] = df['Geography'].map(geography_encoder)

    gender_encoder = {gender: idx for idx, gender in enumerate(df['Gender'].unique())}
    df['Gender'] = df['Gender'].map(gender_encoder)

    local_path = os.path.join(data_wrangling_artifact_path, 'processed_data_head.csv')
    df.head().to_csv(local_path, index=False)
    mlflow.log_artifact(local_path)
    os.remove(local_path)

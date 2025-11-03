import os
import mlflow
import pandas as pd
from sklearn.model_selection import train_test_split
from imblearn.under_sampling import RandomUnderSampler

from dotenv import load_dotenv
load_dotenv()


mlflow.set_tracking_uri('http://localhost:5000')
mlflow.set_experiment('Pré-processamento de Dados')


def split_data(df):
    X = df.drop('Exited', axis=1)
    y = df['Exited']

    seed = 42
    X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.15, random_state=seed, stratify=y)
    X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.15/(1-0.15), random_state=seed, stratify=y_temp)

    rus = RandomUnderSampler(random_state=seed)
    X_val, y_val = rus.fit_resample(X_train, y_train)

    return X_train, X_test, X_val, y_train, y_test, y_val



def data_wrangling(df):
    processed_artifact_path = os.environ['PROCESSED_ARTIFACT_PATH']
    with mlflow.start_run(run_name="Pré-processamento de Dados", nested=True) as run:
    
        df = df.drop(['RowNumber', 'CustomerId', 'Surname'], axis=1)

        geography_encoder = {country: idx for idx, country in enumerate(df['Geography'].unique())}
        df['Geography'] = df['Geography'].map(geography_encoder)

        gender_encoder = {gender: idx for idx, gender in enumerate(df['Gender'].unique())}
        df['Gender'] = df['Gender'].map(gender_encoder)

        local_path = os.path.join(processed_artifact_path, 'processed_data_head.csv')
        df.head().to_csv(local_path, index=False)
        mlflow.log_artifact(local_path)
        os.remove(local_path)

        # local_path = os.path.join(processed_artifact_path, 'processed_data.csv')
        # df.to_csv(local_path, index=False)

        return split_data(df)

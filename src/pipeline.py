import os
import mlflow
import pandas as pd
from dotenv import load_dotenv

from analysis.run_analysis import run_analysis
from preprocessing.data_wrangling import data_wrangling
from models.tuning import tuning


mlflow.set_tracking_uri('http://localhost:5000')
mlflow.set_experiment('Pipeline de Treinamento e Avaliação dos Modelos')


def run_pipeline():
    load_dotenv()

    df = pd.read_csv(os.environ['S3_DATA_LINK'])
    
    with mlflow.start_run(run_name="Pipeline de Treinamento e Avaliação dos Modelos") as run:
        run_analysis(df.copy())
        X_train, X_test, X_val, y_train, y_test, y_val = data_wrangling(df.copy())
        tuning(X_train, X_test, X_val, y_train, y_test, y_val)


run_pipeline()
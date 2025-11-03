import os
import joblib
import optuna
import mlflow
import numpy as np
import pandas as pd
from dotenv import load_dotenv
from warnings import simplefilter
from sklearn.metrics import confusion_matrix, f1_score, accuracy_score, precision_score, recall_score

from models.models_config import baseline_models, param_grids

from tracking.artifact_generation import (
    save_confusion_matrix, 
    save_classification_report, 
    save_train_vs_val_overview, 
    save_detailed_overview, 
    save_cost_overview
)

"""
[BEGIN] Config
"""

load_dotenv()
simplefilter(action='ignore')
optuna.logging.set_verbosity(optuna.logging.WARNING)

"""
[END] Config
"""

"""
[BEGIN] Functions
"""

def calculate_model_cost(cm):
    cost_matrix = [[0, 230], [791.40, 0]]

    return np.sum(cm * cost_matrix)


def objective(trial, model_instance, param_grid, X_train, y_train, X_val, y_val):
    params = param_grid(trial)
    clf = model_instance.__class__(**params)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_val)

    train_f1 = f1_score(y_train, clf.predict(X_train))
    trial.set_user_attr("train_f1_score", train_f1)
    
    return f1_score(y_val, y_pred)


def predict(clf, X_test, y_test):
    prediction = clf.predict(X_test)
    acc_test = accuracy_score(y_test, prediction)
    precision_test = precision_score(y_test, prediction, average='weighted')
    recall_test = recall_score(y_test, prediction, average='weighted')
    f1_test = f1_score(y_test, prediction, average='weighted')

    return prediction, acc_test, precision_test, recall_test, f1_test

"""
[END] Functions
"""

def tuning(X_train, X_test, X_val, y_train, y_test, y_val):
    with mlflow.start_run(run_name='Treinamento e Otimização dos Modelos', nested=True) as run:
        cost_results = dict()

        """
        [BEGIN] Modelos Baseline
        """

        processed_artifact_path = os.environ['PROCESSED_ARTIFACT_PATH']
        for key in baseline_models.keys():
            model = baseline_models[key]
            # Treina o modelo
            model.fit(X_train, y_train)
            train_prediction, acc_train, precision_train, recall_train, f1_train = predict(model, X_train, y_train)

            # Faz o log das métricas de treino
            train_metrics = {
                'train_accuracy_score': acc_train,
                'train_precision': precision_train,
                'train_recall': recall_train,
                'train_f1': f1_train
            }
            mlflow.log_metrics(train_metrics)
            
            # Faz a previsão e o log das métricas de teste
            test_prediction, acc_test, precision_test, recall_test, f1_test = predict(model, X_test, y_test)
            test_metrics = {
                'test_accuracy_score': acc_test,
                'test_precision': precision_test,
                'test_recall': recall_test,
                'test_f1': f1_test
            }
            mlflow.log_metrics(test_metrics)

            artifact_path = f'Baseline_{key}'

            local_path = os.path.join(processed_artifact_path, f'{artifact_path} confusion matrix.png')
            cm = confusion_matrix(y_test, test_prediction)
            save_confusion_matrix(cm, f"Matriz de Confusão - {key}", local_path, artifact_path)

            local_path = os.path.join(processed_artifact_path, f'Baseline_{key} classification report.png')
            save_classification_report(y_test, test_prediction, local_path, artifact_path)

            cost_results[f"Baseline_{key}"] = calculate_model_cost(cm)

            mlflow.sklearn.log_model(
                sk_model=model,
                name=f'baseline_{key}',
                input_example=X_train[:5]
            )

        """
        [END] Modelos Baseline
        """

        """
        [BEGIN] Otimização dos Modelos
        """

        tuning_results = dict()
        for model_name, clf_data in list(param_grids.items()):
            print(f'Otimizando: {model_name}')
            study = optuna.create_study(direction='maximize')
            
            study.optimize(
                lambda trial: objective(
                    trial, 
                    clf_data['model_instance'], 
                    clf_data['params'],
                    X_train, 
                    y_train, 
                    X_val, 
                    y_val
                ), 
                n_trials=300
            )

            tuning_results[model_name] = dict()
            tuning_results[model_name]['best_params'] = study.best_params
            tuning_results[model_name]['trials'] = study.trials_dataframe()

        """
        [END] Otimização dos Modelos
        """

        """
        [BEGIN] Avaliação dos Modelos
        """

        for key, value in tuning_results.items():
            results = tuning_results[key]
            best_params = results['best_params']
            
            model = param_grids[key]['model_instance'].__class__(**best_params)
            model.fit(X_train, y_train)
            train_prediction, acc_train, precision_train, recall_train, f1_train = predict(model, X_train, y_train)
            train_metrics = {
                'train_accuracy_score': acc_train,
                'train_precision': precision_train,
                'train_recall': recall_train,
                'train_f1': f1_train
            }
            mlflow.log_metrics(train_metrics)

            mlflow.sklearn.log_model(
                sk_model=model,
                name=f'baseline_{key}',
                input_example=X_train[:5]
            )

            # Faz o log das métricas de teste
            test_prediction, acc_test, precision_test, recall_test, f1_test = predict(model, X_test, y_test)
            test_metrics = {
                'test_accuracy_score': acc_test,
                'test_precision': precision_test,
                'test_recall': recall_test,
                'test_f1': f1_test
            }
            mlflow.log_metrics(test_metrics)

            artifact_path = f'Optimized_{key}'

            local_path = os.path.join(processed_artifact_path, f'{artifact_path} classification report.csv')
            save_classification_report(y_test, test_prediction, local_path, artifact_path)

            cm = confusion_matrix(y_test, test_prediction)
            local_path = os.path.join(processed_artifact_path, f'{artifact_path} confusion matrix.png')
            save_confusion_matrix(cm, f"Matriz de Confusão - {key}", local_path, artifact_path)

            cost_result = calculate_model_cost(cm)
            cost_results[f"Optmized_{key}"] = cost_result

        local_path = os.path.join(processed_artifact_path, f'Cost Overview.csv')
        artifact_path = 'cost_overview'
        save_cost_overview(cost_results, local_path, artifact_path)

        for key, value in tuning_results.items():
            data = tuning_results[key]
            
            local_path = os.path.join(processed_artifact_path, f'f1score_tuning_comparisson.png')
            save_train_vs_val_overview(data['trials'], key, local_path)

            local_path = os.path.join(processed_artifact_path, f'f1score_by_hyperparameter.png')
            save_detailed_overview(data['trials'], key, local_path)

        """
        [END] Avaliação dos Modelos
        """


        best_model_name = min(cost_results, key=lambda k: cost_results[k]['cost'] if isinstance(cost_results[k], dict) and 'cost' in cost_results[k] else float('inf'))

        model_name = None
        if best_model_name.startswith('Optmized_'):
            # Modelo otimizado
            model_name = best_model_name.replace('Optmized_', '')
            params = tuning_results[model_name]['best_params']
            model_instance = param_grids[model_name]['model_instance'].__class__(**params)
        else:
            # Modelo baseline
            model_name = best_model_name.replace('Baseline_', '')
            model_instance = baseline_models[model_name]
            params = model_instance.get_params()
            model_instance = model_instance.__class__(**params)

        model_instance.fit(X_train, y_train)

        joblib.dump(model_instance, f'{os.environ['PKL_PATH']}/{model_name}.pkl')
        mlflow.log_artifact(
            f'{os.environ["PKL_PATH"]}/{model_name}.pkl'
        )


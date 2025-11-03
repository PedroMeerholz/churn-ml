import os
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.metrics import classification_report
import mlflow
import math


def save_confusion_matrix(cm, title, local_path, artifact_path=None):
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['neg', 'pos'], yticklabels=['neg', 'pos'])
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.title(title)
    plt.savefig(f"{local_path}")
    plt.close()

    save_artifact(local_path, artifact_path)


def save_classification_report(y_test, prediction, local_path, artifact_path=None):
    report = classification_report(y_test, prediction, output_dict=True)
    report = pd.DataFrame(report).transpose()
    report.reset_index(inplace=True)
    report.columns = ['reference', 'precision', 'recall', 'f1-score', 'support']
    report.to_csv(local_path)
    
    save_artifact(local_path, artifact_path)


def save_train_vs_val_overview(trials_df, model_name, local_path, artifact_path=None):
    plt.figure(figsize=(12, 6))
    plt.plot(trials_df['number'], trials_df['user_attrs_train_f1_score'], label='F1 Score Treino', marker='o')
    plt.plot(trials_df['number'], trials_df['value'], label='F1 Score Validação', marker='o')
    plt.xlabel("Número do Trial")
    plt.ylabel("F1 Score")
    plt.title("Comparativo de F1 Score: Treino vs Validação durante a Otimização")
    plt.legend()
    plt.grid(True)
    plt.suptitle(model_name)
    plt.tight_layout()
    plt.savefig(f"{local_path}")
    plt.close()

    save_artifact(local_path, artifact_path)


def save_detailed_overview(trials_df, model_name, local_path, artifact_path=None):
    # Seleciona apenas as colunas dos hiperparâmetros reais (ignora colunas auxiliares como 'params_str')
    param_cols = [col for col in trials_df.columns if col.startswith('params_') and col != 'params_str']
    num_params = len(param_cols)

    ncols = 2
    nrows = math.ceil(num_params / ncols)
    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(14, nrows * 5))
    axes = axes.flatten()

    for i, param in enumerate(param_cols):
        ax = axes[i]
        # Agrupa por valor do parâmetro e calcula a média do valor objetivo ('value')
        grouped = trials_df.groupby(param)['value'].mean().reset_index()
        ax.plot(grouped[param], grouped['value'], marker='o', linestyle='-')
        ax.set_title(f"Métrica vs {param.replace('params_', '')}")
        ax.set_xlabel(param.replace('params_', ''))
        ax.set_ylabel("F1 Score da Validação")
        ax.grid(True)

    # Oculta os eixos não utilizados
    for j in range(num_params, len(axes)):
        axes[j].axis('off')

    plt.suptitle(model_name)
    plt.tight_layout()
    plt.savefig(f"{local_path}")
    plt.close()

    save_artifact(local_path, artifact_path)


def save_cost_overview(cost_results, local_path, artifact_path=None):
    cost_results_df = pd.DataFrame(list(cost_results.items()), columns=['Modelo', 'Custo dos Erros'])
    cost_results_df = cost_results_df.sort_values(by='Custo dos Erros', ascending=True)
    cost_results_df.reset_index(drop=True, inplace=True)
    cost_results_df['Custo dos Erros'] = cost_results_df['Custo dos Erros'].apply(lambda x: f"R$ {x:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
    cost_results_df.to_csv(local_path, index=False)

    save_artifact(local_path, artifact_path)


def save_artifact(local_path, artifact_path=None):
    if artifact_path is None:
        mlflow.log_artifact(local_path)
    else:
        mlflow.log_artifact(local_path, artifact_path)
    os.remove(local_path)


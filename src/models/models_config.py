from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier, BaggingClassifier, ExtraTreesClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier


seed = 42
baseline_models = {
    "Random Forest": RandomForestClassifier(n_estimators=100, random_state=seed),
    "Gradient Boosting": GradientBoostingClassifier(n_estimators=100, random_state=seed),
    "AdaBoost": AdaBoostClassifier(n_estimators=100, random_state=seed),
    "Bagging": BaggingClassifier(n_estimators=100, random_state=seed),
    "Extra Trees": ExtraTreesClassifier(n_estimators=100, random_state=seed),
    "XGBoost": XGBClassifier(use_label_encoder=False, eval_metric='logloss', random_state=seed),
    "LightGBM": LGBMClassifier(random_state=seed),
}

param_grids = {
    "Random Forest": {
        "model_instance": RandomForestClassifier(verbose=0),
        "params": lambda trial:{
            "n_estimators": trial.suggest_int("n_estimators", 50, 300),
            "max_depth": trial.suggest_int("max_depth", 2, 32, log=True),
            "min_samples_split": trial.suggest_int("min_samples_split", 2, 20),
            "min_samples_leaf": trial.suggest_int("min_samples_leaf", 1, 20),
            "bootstrap": trial.suggest_categorical("bootstrap", [True, False]),
        }
    },
    "Gradient Boosting": {
        "model_instance": GradientBoostingClassifier(verbose=0),
        "params": lambda trial:{
            "n_estimators": trial.suggest_int("n_estimators", 50, 300),
            "learning_rate": trial.suggest_float("learning_rate", 1e-3, 1.0),
            "max_depth": trial.suggest_int("max_depth", 2, 16),
            "subsample": trial.suggest_float("subsample", 0.5, 1.0),
            "min_samples_split": trial.suggest_int("min_samples_split", 2, 20),
            "min_samples_leaf": trial.suggest_int("min_samples_leaf", 1, 20),
        }
    },
    "AdaBoost": {
        "model_instance": AdaBoostClassifier(),
        "params": lambda trial:{
            "n_estimators": trial.suggest_int("n_estimators", 50, 300),
            "learning_rate": trial.suggest_float("learning_rate", 1e-3, 1.0),
        }
    },
    "Bagging": {
        "model_instance": BaggingClassifier(verbose=0),
        "params": lambda trial:{
            "n_estimators": trial.suggest_int("n_estimators", 10, 200),
            "max_samples": trial.suggest_float("max_samples", 0.5, 1.0),
            "max_features": trial.suggest_float("max_features", 0.5, 1.0),
            "bootstrap": trial.suggest_categorical("bootstrap", [True, False]),
        }
    },
    "Extra Trees": {
        "model_instance": ExtraTreesClassifier(verbose=0),
        "params": lambda trial:{
            "n_estimators": trial.suggest_int("n_estimators", 50, 300),
            "max_depth": trial.suggest_int("max_depth", 2, 32, log=True),
            "min_samples_split": trial.suggest_int("min_samples_split", 2, 20),
            "min_samples_leaf": trial.suggest_int("min_samples_leaf", 1, 20),
            "bootstrap": trial.suggest_categorical("bootstrap", [True, False]),
        }
    },
    "XGBoost": {
        "model_instance": XGBClassifier(verbosity=0, use_label_encoder=False),
        "params": lambda trial:{
            "n_estimators": trial.suggest_int("n_estimators", 50, 300),
            "max_depth": trial.suggest_int("max_depth", 2, 16),
            "learning_rate": trial.suggest_float("learning_rate", 1e-3, 1.0),
            "subsample": trial.suggest_float("subsample", 0.5, 1.0),
            "colsample_bytree": trial.suggest_float("colsample_bytree", 0.5, 1.0),
            "gamma": trial.suggest_float("gamma", 1e-8, 1.0),
            "reg_alpha": trial.suggest_float("reg_alpha", 1e-8, 1.0),
            "reg_lambda": trial.suggest_float("reg_lambda", 1e-8, 1.0),
        }
    },
    "LightGBM": {
        "model_instance": LGBMClassifier(),
        "params": lambda trial:{
            "n_estimators": trial.suggest_int("n_estimators", 50, 300),
            "max_depth": trial.suggest_int("max_depth", 2, 32),
            "learning_rate": trial.suggest_float("learning_rate", 1e-3, 1.0),
            "num_leaves": trial.suggest_int("num_leaves", 7, 256),
            "subsample": trial.suggest_float("subsample", 0.5, 1.0),
            "colsample_bytree": trial.suggest_float("colsample_bytree", 0.5, 1.0),
            "reg_alpha": trial.suggest_float("reg_alpha", 1e-8, 1.0),
            "reg_lambda": trial.suggest_float("reg_lambda", 1e-8, 1.0),
        }
    },
}
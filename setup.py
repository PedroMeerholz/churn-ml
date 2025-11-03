import os
from dotenv import load_dotenv


load_dotenv()


data_dir = os.environ['DATA_DIR_PATH']
pkl_dir = os.environ['PKL_PATH']

os.makedirs(data_dir, exist_ok=True)
os.makedirs(os.path.join(data_dir, 'analysis'), exist_ok=True)
os.makedirs(os.path.join(data_dir, 'processed'), exist_ok=True)

os.makedirs(os.path.join('src'), exist_ok=True)
os.makedirs(os.path.join('src', 'models'), exist_ok=True)
os.makedirs(os.path.join('src', 'pipelines'), exist_ok=True)

os.makedirs(os.path.join(analysis_artifact_path, 'analise_demografica'), exist_ok=True)
os.makedirs(os.path.join(analysis_artifact_path, 'analise_geografica_e_de_produto'), exist_ok=True)
os.makedirs(os.path.join(analysis_artifact_path, 'analise_comportamental'), exist_ok=True)
os.makedirs(os.path.join(analysis_artifact_path, 'qualidade_dos_dados'), exist_ok=True)

os.makedirs(pkl_dir, exist_ok=True)

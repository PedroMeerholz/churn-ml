import os
from dotenv import load_dotenv


load_dotenv()


data_dir = os.environ['DATA_DIR_PATH']

os.makedirs(data_dir, exist_ok=True)
os.makedirs(os.path.join(data_dir, 'analysis'), exist_ok=True)
os.makedirs(os.path.join(data_dir, 'processed'), exist_ok=True)

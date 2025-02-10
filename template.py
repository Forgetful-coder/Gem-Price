import logging 
from pathlib import Path
import os


logging.basicConfig(level = logging.INFO, format='[%(asctime)s]:%(message)s:')


list_of_files=[
    '.github/workflows/main.yaml',
    'requirements_dev.txt',
    'requirements.txt',
    'src/__init__.py',
    'src/components/__init__.py',
    'src/components/data_ingestion.py',
    'src/components/data_transformation.py',
    'src/components/data_validation.py',
    'src/components/model_trainer.py',
    'src/components/model_evaluation.py',
    'src/logger/__init__.py',
    'src/logger/logger.py',
    'src/exceptions/__init__.py',
    'src/exceptions/exceptions.py',
    'src/experiments/experiments.ipynb',
    'src/pipeline/__init__.py',
    'src/pipeline/train_pipeline.py',
    'src/pipeline/batch_prediction.py',
    "tests/__init__.py",
    "tests/unit/__init__.py",
    "tests/integration/__init__.py",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "init_setup.sh"
]

for file_path in list_of_files:
    file_path=Path(file_path)
    file_dir,file_name = os.path.split(file_path)

    if file_dir!='':
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f'File Directory for {file_dir} created.')
    
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,'w') as f:
            pass
        logging.info(f'Creating an empty file {file_name}')
    else:
        logging.info(f'{file_name} already exists')
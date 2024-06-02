import os
from pathlib import Path

files = [".github/workflows/.gitkeep", 
        "src/__init__.py", 
        "src/components/__init__.py",
        "src/components/data_ingestion.py" ,
        "src/components/data_transform.py" ,
        "src/components/model_train.py" ,
        "src/components/model_eval.py",
        "src/pipeline/__init__.py",
        "src/pipeline/training.py"
        "src/pipeline/prediction.py",
        "src/logger/logging.py",
        "src/exception/exception",
        "src/utils/__init__.py" ,
        "src/utils/utils.py" ,
        "test/unit/__init__.py",
        "test/integration/__init__.py",
        "init_setup.sh",
        "requirements.txt",
        "requirement_dev.txt",
        "setup.py",
        "setup.cfg",
        "pyproject.toml",
        "tox.ini" ,
        "experiment/experiments.ipynb"]

for filepath in files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass 

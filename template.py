import os
from pathlib import Path 
import logging

logging.basicConfig(level=logging.INFO, format="[%(asctime)s] : %(message)s : ")

list_file = [
    ".gitignore",
    "src/__init__.py",
    "src/pipeline.py",
    "src/prompt.py",
    "src/llm.py",
    "configuration/config.toml",
    "app.py",
    "experiments/experiments.ipynb",
    "logs/.gitkeep",
    "README.md",
    'requirements.txt',
    "Dockerfile",
    ".dockerignore"
]

for file in list_file:
    file_path = Path(file)
    filepath, filename = os.path.split(file_path)
    if filepath != "":
        os.makedirs(filepath,exist_ok=True)
        logging.info(f"creating directory : {filepath} for file : {filename}")

    if (not os.path.exists(filepath) or os.path.getsize(filepath)==0):
        with open(file_path,"w") as f:
            pass
            logging.info(f"Creating empty file: {filename}")

    else:
        logging.info(f"{filename} is already exists.")
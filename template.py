import os
from pathlib import Path
import logging

# Logs generator with the time where the error occured and the message of the errror
logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')


project_name = "CNN_Classification_Task"

# List of files and folder we need to create
list_of_files = [
    # Needed for yaml files for deployement
    ".github/workflows/.gitkeep",
    #  __init__.py is a constructor file to create packages
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]


for filepath in list_of_files:
    # Transform the paths we wrote in Windows usable paths to be created 
    filepath = Path(filepath)
    # We separate the folders from the files
    filedir, filename = os.path.split(filepath)

    # If the folder has a name we create the directory
    if filedir != "":

        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory {filedir} for the file {filename}")
    # If the file doesn't exist
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        # We create the file
        with open(filepath, "w") as f:
            # Create empty file
            pass
            logging.info(f"Creating empty file {filepath}")

    else:
        logging.info(f"{filename} already exists")
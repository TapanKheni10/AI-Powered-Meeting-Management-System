import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

project_name = "MeetingManagement"

## These is a list of the files that will be created
list_of_files = [
    "pages",
    "app.py",
    f"src/{project_name}",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/services",
    f"src/{project_name}/services/__init__.py",
    f"src/{project_name}/services/agenda_service.py",
    f"src/{project_name}/services/meeting_service.py",
    f"src/{project_name}/services/summary_service.py",

    f"src/{project_name}/constants",
    f"src/{project_name}/constants/__init__.py",

    "requirements.txt",
    "setup.py",

]

for file_path in list_of_files:
    if "." in file_path:
        Path(file_path).touch()
        logging.info(f"Created file at {file_path}")
    else:
        os.makedirs(file_path, exist_ok=True)
    logging.info(f"Created directory at {file_path}")
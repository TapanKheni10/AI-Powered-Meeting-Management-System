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
    f"src/{project_name}/servies",
    f"src/{project_name}/servies/__init__.py",
    f"src/{project_name}/servies/document_service.py",
    f"src/{project_name}/servies/meeting_service.py",
    f"src/{project_name}/servies/llm_service.py",
    f"src/{project_name}/servies/summary_service.py",

    f"src/{project_name}/utils",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/database.py",
    f"src/{project_name}/utils/vector_store.py",

    f"src/{project_name}/models",
    f"src/{project_name}/models/__init__.py",
    f"src/{project_name}/models/document.py",
    f"src/{project_name}/models/meeting.py",
    f"src/{project_name}/models/user.py",
]

for file_path in list_of_files:
    if "." in file_path:
        Path(file_path).touch()
        logging.info(f"Created file at {file_path}")
    else:
        os.makedirs(file_path, exist_ok=True)
    logging.info(f"Created directory at {file_path}")
echo[$(date)] : "Setting up the intial setup for the project"

echo[$(date)] : "Creating the virtual environment with python version 3.9.6"

conda create -n venv python=3.9.6

echo[$(date)] : "Activating the virtual environment"

conda activate venv

echo[$(date)] : "Upgrading pip setuptools and wheel"

pip install --upgrade pip setuptools wheel

echo[$(date)] : "Installing the requirements"

pip install -r requirements.txt

echo[$(date)] : "Initial setup completed"


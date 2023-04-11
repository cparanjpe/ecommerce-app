# Create a virtual environment
python -m venv myenv

# Activate the virtual environment
(for windows PowerShell)
ProjectEnv\Scripts\activate.ps1 

# Deactivate the virtual environment
deactivate

# installed packages info
pip freeze
pip freeze > requirements.txt (gives list of all installed packages in txt file)

# install all packages in given file
pip install -r file_name.txt
eg) pip install -r ./vitually_installed.txt
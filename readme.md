# 1. Create a project folder

your folder name and open in ant IDE

# 2. Create a virtual environment

python3 -m venv venv
source venv/bin/activate

# 3. Install Flask and Flask-JWT-Extended

pip install Flask PyJWT pymongo flask-pymongo python-dotenv

# 4. Get the requirements.txt file

pip freeze > requirements.txt

# 5. Folder structure

project/
├── src/
│ ├── controllers/
│ │ ├── auth_controller.py
│ │ ├── user_controller.py
│ │ └── **init**.py
│ ├── models/
│ │ ├── user.py
│ │ └── **init**.py
│ ├── routes/
│ │ ├── auth_routes.py
│ │ ├── user_routes.py
│ │ └── **init**.py
│ ├── **init**.py
│ └── config.py
├── server.py
└── requirements.txt

# 6. Activate your virtual environment, install any additional dependencies from requirements.txt, and run the Flask app:

source venv/bin/activate
pip install -r requirements.txt

# 7. Run the Flask app

python server.py

# 8. add gitignore file to not push this information in git before initializing the git repository

# 8.a. Virtual Environment

venv/
env/

# 8.b. Environment Files

.env

# 8.c. IDE/Editor Files

.vscode/
.idea/
.vs/

# 8.d. Compiled Files or Directories

**pycache**/
.pytest*cache/
*.pyc
\_.pyo

# 8.e. Dependency Files

\*.egg-info/
dist/
build/
requirements.txt
requirements-dev.txt

# 8.f. Log Files

\*.log
logs/

# 8.g. Temporary Files

tmp/
temp/
\*.tmp

# 9. Run the Flask app for production install gunicorn

gunicorn -w 4 -b 127.0.0.1:8080 server:app

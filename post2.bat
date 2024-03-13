


ECHO Creating project directory...
mkdir Flask-Project

ECHO Navigate to the project directory...
cd Flask-Project

ECHO **Python virtual environment creation:**

ECHO Creating virtual environment with venv...
python -m venv .venv





ECHO Create a Python file named main.py...
echo print('Hello Flask') > main.py

call .venv\Scripts\pip install Flask

ECHO Open project directory in VS Code...
code .

ECHO **All set! Start coding your Flask project!**

:script_end
PAUSE
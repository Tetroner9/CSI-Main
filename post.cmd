echo Installing gdown Python Package for downloading setup files...
:: Installs gdown package globally
pip install gdown

echo Downloading Setup Files from Drive...
:: Downloads setup files from google drive
gdown --folder 1Jiz9BBs4ypxa8bwRncFUroE7w_1Ayj3d

echo Installing Vscode...
::
Setup-Files\VSCodeUserSetup-x64-1.87.1.exe /VERYSILENT /NORESTART /MERGETASKS=!runcode

echo Installing Xampp...
:: Installs Xampp
Setup-Files\xampp-windows-x64-8.2.12-0-VS16-installer.exe

echo Deleting Setup files...
:: Removes setup files
setlocal

set /p confirm=Do you want to remove the Setup-Files directory and its contents? (y/n): 
if /i "%confirm%"=="y" (
    rmdir /s /q Setup-Files
    echo Setup-Files directory and its contents removed successfully.
) else (
    echo Removal cancelled. Setup-Files directory and its contents were not removed.
)

endlocal

echo Creating Flask-Project directory...
:: Create Flask-Project directory
mkdir Flask-Project

echo Entering Flask-Project directory...
:: Change directory to Flask-Project
cd Flask-Project

echo Creating Python virtual environment...
:: Create Python virtual environment
python -m venv venv

echo Activating virtual environment...
:: Activate virtual environment
call venv\Scripts\activate

echo Installing required pip packages...
:: Install required pip packages
pip install flask flask-restful

echo Creating main.py file...
:: Create main.py file
echo print("Hello, Flask!") > main.py

echo Opening VS Code...
:: Open VS Code in current directory
start code .

PAUSE
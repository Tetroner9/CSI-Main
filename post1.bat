@ECHO OFF
set CHOCOLATEY_INSTALLED=1

where python > NUL 2>&1 (
  ECHO Python not found. Installing...
  if %CHOCOLATEY_INSTALLED% == 0 (
    powershell -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = [SecurityProtocolSupport]::Tls12; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
    set CHOCOLATEY_INSTALLED=1
  )
  ECHO Installing Python with Chocolatey...
  choco install python -y
) || (
  ECHO Python found. Skipping installation.
)

ECHO Now, let's install the following:
ECHO - XAMPP (web development server) - https://www.apachefriends.org/
ECHO - Visual Studio Code (code editor) - https://code.visualstudio.com/download

start post2.bat

PAUSE
@ECHO OFF

rem Flag to track Chocolatey installation
set CHOCOLATEY_INSTALLED=0

rem Check for Chocolatey
where choco > NUL 2>&1 (
  ECHO Chocolatey not found. Installing...
  powershell -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = [SecurityProtocolSupport]::Tls12; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
  set CHOCOLATEY_INSTALLED=1
)


curl -O -f https://raw.githubusercontent.com/Tetroner9/CSI-Main/main/post1.bat
curl -O -f https://raw.githubusercontent.com/Tetroner9/CSI-Main/main/post2.bat

start post1.bat

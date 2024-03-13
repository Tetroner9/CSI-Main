
$logPath = ".\_install_log.txt"

Out-File -FilePath $logPath -Append

# Check internet connection
if (!(Test-Connection -ComputerName google.com -Count 1 -Quiet)) {
  Write-Host "Error: No internet connection detected. Exiting..." >> $logPath
  Exit
}

# Check if winget is available
if (Test-Path ~\AppData\Local\Microsoft\WindowsApps\winget.exe) {
  Write-Host "Winget is already installed."
} else {
  # Check Windows version (optional, edit based on your requirements)
  $osVersion = Get-Version (Get-WmiObject Win32_OperatingSystem).Version
  if ($osVersion -lt (New-Version "10.0.1809")) {
    Write-Host "Winget is not supported on this version of Windows (pre-1809)"
    Exit
  }

  # Install Winget
  Write-Host "Winget not found, installing it now..."
  Start-Process "ms-appinstaller:?source=https://aka.ms/getwinget" -Wait
  Write-Host "Winget installed successfully!"
}

# Install software using winget with specific versions
$softwareList = @("Python.Python.3.12", "ApacheFriends.Xampp.8.2", "Microsoft.VisualStudioCode")

foreach ($software in $softwareList) {
  # Check if software is already installed
  if (!(winget list | Where-Object { $_.Id -eq $software })) {
    Write-Host "Installing $software..."
    winget install $software 
    Write-Host "$software installed successfully!"
  } else {
    Write-Host "$software is already installed."
  }
}

$downloadUrl = "https://raw.githubusercontent.com/Tetroner9/CSI-Main/main/post.bat"
$downloadPath = ".\"

$webClient = New-Object System.Net.WebClient
$webClient.DownloadFile($downloadUrl, $downloadPath + "\post.bat")

Write-Host "post.bat downloaded successfully."


Write-Host "All checks and installations completed!"

Start-Process "post.bat" 

Write-Host "All checks and installations completed!" >> $logPath

Exit
<#
.SYNOPSIS
    Exports basic system information to a text file.

.PARAMETER OutputFile
    Path to the output file.

.EXAMPLE
    .\export_system_info.ps1 -OutputFile "C:\SysInfo\report.txt"
#>

param (
    [Parameter(Mandatory=$true)]
    [string]$OutputFile
)

$sysInfo = @()
$sysInfo += "Date: $(Get-Date)"
$sysInfo += "Computer Name: $env:COMPUTERNAME"
$sysInfo += "User: $env:USERNAME"
$sysInfo += "OS Version: $(Get-CimInstance Win32_OperatingSystem | Select-Object -ExpandProperty Caption)"
$sysInfo += "CPU: $(Get-CimInstance Win32_Processor | Select-Object -ExpandProperty Name)"
$sysInfo += "RAM (GB): $([math]::Round((Get-CimInstance Win32_ComputerSystem).TotalPhysicalMemory / 1GB, 2))"
$sysInfo += "Uptime: $((Get-Date) - (gcim Win32_OperatingSystem).LastBootUpTime)"
$sysInfo += "Disk Usage:"
$sysInfo += Get-PSDrive -PSProvider FileSystem | ForEach-Object {
    "$($_.Name): Used $([math]::Round($_.Used/1GB, 2)) GB / $([math]::Round($_.Used + $_.Free/1GB, 2)) GB"
}

$sysInfo | Out-File -FilePath $OutputFile -Encoding UTF8
Write-Host "System info written to: $OutputFile"

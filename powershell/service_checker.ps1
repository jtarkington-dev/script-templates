<#
.SYNOPSIS
    Checks if a Windows service is running and restarts it if it's not.

.PARAMETER ServiceName
    The name of the service to check.

.EXAMPLE
    .\service_checker.ps1 -ServiceName "Spooler"
#>

param (
    [Parameter(Mandatory=$true)]
    [string]$ServiceName
)

try {
    $service = Get-Service -Name $ServiceName -ErrorAction Stop
} catch {
    Write-Error "Service '$ServiceName' not found."
    exit 1
}

if ($service.Status -ne 'Running') {
    Write-Host "Service '$ServiceName' is not running. Attempting to start..."
    try {
        Start-Service -Name $ServiceName
        Write-Host "Service started."
    } catch {
        Write-Error "Failed to start service: $_"
    }
} else {
    Write-Host "Service '$ServiceName' is already running."
}

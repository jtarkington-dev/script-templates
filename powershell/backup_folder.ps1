<#
.SYNOPSIS
    Creates a backup of a source folder into a date-stamped destination.

.PARAMETER SourcePath
    Folder to back up.

.PARAMETER DestinationRoot
    Where the backup folder will be created.

.EXAMPLE
    .\backup_folder.ps1 -SourcePath "C:\Data" -DestinationRoot "D:\Backups"
#>

param (
    [Parameter(Mandatory=$true)]
    [string]$SourcePath,

    [Parameter(Mandatory=$true)]
    [string]$DestinationRoot
)

if (-Not (Test-Path $SourcePath)) {
    Write-Error "Source folder not found: $SourcePath"
    exit 1
}

$timestamp = Get-Date -Format "yyyy-MM-dd_HH-mm-ss"
$backupFolder = Join-Path $DestinationRoot "Backup_$timestamp"

try {
    Copy-Item -Path $SourcePath -Destination $backupFolder -Recurse
    Write-Host "Backup completed: $backupFolder"
} catch {
    Write-Error "Backup failed: $_"
}

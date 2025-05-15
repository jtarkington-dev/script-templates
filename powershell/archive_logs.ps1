<#
.SYNOPSIS
    Compresses all .log files in a given directory into a ZIP archive.

.PARAMETER LogDir
    Folder containing .log files to compress.

.PARAMETER OutputZip
    Full path to the ZIP file to create.

.EXAMPLE
    .\archive_logs.ps1 -LogDir "C:\Logs" -OutputZip "C:\Archive\logs.zip"
#>

param (
    [Parameter(Mandatory=$true)]
    [string]$LogDir,

    [Parameter(Mandatory=$true)]
    [string]$OutputZip
)

if (-Not (Test-Path $LogDir)) {
    Write-Error "Log directory does not exist: $LogDir"
    exit 1
}

Add-Type -AssemblyName 'System.IO.Compression.FileSystem'
$zip = [System.IO.Compression.ZipFile]::CreateFromDirectory

$logsToArchive = Get-ChildItem -Path $LogDir -Filter *.log -File

if ($logsToArchive.Count -eq 0) {
    Write-Host "No .log files found in $LogDir."
    exit 0
}

$tempDir = Join-Path $env:TEMP "log_archive_$((Get-Random))"
New-Item -ItemType Directory -Path $tempDir | Out-Null

foreach ($file in $logsToArchive) {
    Copy-Item $file.FullName -Destination $tempDir
}

[System.IO.Compression.ZipFile]::CreateFromDirectory($tempDir, $OutputZip)
Remove-Item $tempDir -Recurse -Force

Write-Host "Archived logs to: $OutputZip"

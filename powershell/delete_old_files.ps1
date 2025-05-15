<#
.SYNOPSIS
    Deletes files older than a specified number of days from a target directory.

.PARAMETER TargetFolder
    The directory to clean up.

.PARAMETER DaysOld
    Files older than this number of days will be deleted.

.EXAMPLE
    .\delete_old_files.ps1 -TargetFolder "C:\Temp" -DaysOld 30
#>

param (
    [Parameter(Mandatory=$true)]
    [string]$TargetFolder,

    [Parameter(Mandatory=$true)]
    [int]$DaysOld
)

Write-Host "Cleaning files older than $DaysOld days in: $TargetFolder"

if (-Not (Test-Path $TargetFolder)) {
    Write-Error "The specified folder does not exist: $TargetFolder"
    exit 1
}

$deletedCount = 0
$cutoffDate = (Get-Date).AddDays(-$DaysOld)

Get-ChildItem -Path $TargetFolder -Recurse -File | Where-Object {
    $_.LastWriteTime -lt $cutoffDate
} | ForEach-Object {
    try {
        Remove-Item $_.FullName -Force
        Write-Host "Deleted: $($_.FullName)"
        $deletedCount++
    } catch {
        Write-Warning "Failed to delete: $($_.FullName) - $_"
    }
}

Write-Host "Cleanup complete. $deletedCount files deleted."

# Portfolio Simulation Runner
# Runs the SDG portfolio Monte Carlo simulation and generates a report

Write-Host ("=" * 60) -ForegroundColor Cyan
Write-Host "SDG Portfolio Simulation" -ForegroundColor Cyan
Write-Host ("=" * 60) -ForegroundColor Cyan
Write-Host ""

# Change to script directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $scriptDir

# Check if Python is available
try {
    $pythonVersion = python --version 2>&1
    Write-Host "Using: $pythonVersion" -ForegroundColor Green
}
catch {
    Write-Host "Error: Python is not installed or not in PATH" -ForegroundColor Red
    exit 1
}

# Check if numpy is installed
Write-Host "Checking dependencies..." -ForegroundColor Yellow
$numpyCheck = python -c "import numpy; print(f'numpy {numpy.__version__}')" 2>&1
if ($LASTEXITCODE -ne 0) {
    Write-Host "Installing numpy..." -ForegroundColor Yellow
    pip install numpy
}
else {
    Write-Host "Found: $numpyCheck" -ForegroundColor Green
}

Write-Host ""
Write-Host "Starting simulation..." -ForegroundColor Yellow
Write-Host ""

# Run the simulation
$startTime = Get-Date
python -m simulation.main
$endTime = Get-Date
$duration = $endTime - $startTime

Write-Host ""
Write-Host ("=" * 60) -ForegroundColor Cyan

if ($LASTEXITCODE -eq 0) {
    Write-Host "Simulation completed successfully!" -ForegroundColor Green
    Write-Host "Duration: $($duration.TotalSeconds.ToString('F1')) seconds" -ForegroundColor Green
    
    # Check if report was generated
    $reportPath = Join-Path $scriptDir "projection_report.md"
    if (Test-Path $reportPath) {
        Write-Host "Report saved to: $reportPath" -ForegroundColor Green
        Write-Host ""
        Write-Host "To view the report, run:" -ForegroundColor Yellow
        Write-Host "  code projection_report.md" -ForegroundColor White
        Write-Host "  # or" -ForegroundColor Gray
        Write-Host "  notepad projection_report.md" -ForegroundColor White
    }
}
else {
    Write-Host "Simulation failed with exit code: $LASTEXITCODE" -ForegroundColor Red
}

Write-Host ("=" * 60) -ForegroundColor Cyan

# SDG Portfolio Sensitivity Analysis
# 
# Runs Monte Carlo simulations with three NAV parameter scenarios:
# - Pessimistic: 3% return, 22% volatility
# - Base case: 5% return, 17% volatility
# - Optimistic: 7% return, 15% volatility
#
# Usage:
#   .\sensitivity.ps1
#
# Output files are saved to the simulation folder:
#   - simulation\projection_report_pessimistic.md
#   - simulation\projection_report_base.md
#   - simulation\projection_report_optimistic.md
#   - simulation\sensitivity_analysis_summary.md

Write-Host "================================================" -ForegroundColor Cyan
Write-Host "SDG Portfolio Sensitivity Analysis" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Run the sensitivity analysis module
python -m simulation.sensitivity_analysis

if ($LASTEXITCODE -eq 0) {
    Write-Host ""
    Write-Host "================================================" -ForegroundColor Green
    Write-Host "Sensitivity analysis completed successfully!" -ForegroundColor Green
    Write-Host "================================================" -ForegroundColor Green
    Write-Host ""
    Write-Host "Output files:" -ForegroundColor Yellow
    Write-Host "  simulation\projection_report_pessimistic.md"
    Write-Host "  simulation\projection_report_base.md"
    Write-Host "  simulation\projection_report_optimistic.md"
    Write-Host "  simulation\sensitivity_analysis_summary.md"
} else {
    Write-Host ""
    Write-Host "================================================" -ForegroundColor Red
    Write-Host "Sensitivity analysis failed with exit code $LASTEXITCODE" -ForegroundColor Red
    Write-Host "================================================" -ForegroundColor Red
    exit $LASTEXITCODE
}

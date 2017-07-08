$start = (Get-Date).Milisecond
For ($i=0; $i -lt 174; $i++){
    Write-Host $i
    python .\get_cards_prices.py
    Write-Host "Waiting... 3 seconds before next iteration..."
    Start-Sleep -s 3
}
$end = (Get-Date).Milisecond
Write-Host "This script took $($end - $start) miliseconds to run."
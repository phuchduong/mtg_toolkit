$start = (Get-Date).Milisecond
For ($i=0; $i -lt 195; $i++){
    Write-Host $i
    python .\get_cards_prices.py
}
$end = (Get-Date).Milisecond
Write-Host "This script took $($end - $start) miliseconds to run."
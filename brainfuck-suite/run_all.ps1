# Run non-interactive Brainfuck modules sequentially
$base = Join-Path $PSScriptRoot '.'
Write-Host "Running Hello World..."
python "$base\run_bf.py" "$base\modules\hello_world.bf"
Write-Host "\nRunning Fibonacci..."
python "$base\run_bf.py" "$base\modules\fibonacci.bf"
Write-Host "\nRunning Multiplication..."
python "$base\run_bf.py" "$base\modules\multiplication.bf"
Write-Host "\nRunning Caesar encode (example input 'A')..."
# Provide 'A' (65) as input
[System.IO.File]::WriteAllBytes('in.bin', (,[byte]65))
Get-Content -Encoding Byte in.bin | python "$base\run_bf.py" "$base\modules\caesar_encode.bf"
Remove-Item in.bin -ErrorAction SilentlyContinue

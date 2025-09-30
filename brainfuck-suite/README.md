# Brainfuck Computational Suite

A small educational suite demonstrating algorithms implemented in Brainfuck.

Contents:
- run_bf.py - a tiny Python Brainfuck interpreter and CLI
- modules/ - Brainfuck program files:
  - hello_world.bf
  - fibonacci.bf
  - multiplication.bf
  - char_io.bf
  - calculator_add.bf
  - caesar_encode.bf

How to run:

1. Run Hello World:

    python run_bf.py modules/hello_world.bf

2. Run Fibonacci:

    python run_bf.py modules/fibonacci.bf

3. Run multiplication:


  - python -m pytest -q

Windows PowerShell examples (from repository root):

     python .\brainfuck-suite\run_bf.py .\brainfuck-suite\modules\hello_world.bf

Pipe binary input (example for calculator_add):

     # write two bytes (4 and 5) to a file then pipe
     [System.IO.File]::WriteAllBytes('in.bin', (,[byte]4 + [byte]5)) ; Get-Content -Encoding Byte in.bin | python .\brainfuck-suite\run_bf.py .\brainfuck-suite\modules\calculator_add.bf

Quick-run helper (PowerShell):

     .\brainfuck-suite\run_all.ps1

    type text and pipe it: echo "hello" | python run_bf.py modules/char_io.bf

5. Run calculator add (provides two bytes):

    printf "\x04\x05" | python run_bf.py modules/calculator_add.bf

Notes:
- This interpreter is minimal and intended for educational use.
- Brainfuck programs here may require adaptation for full correctness; they are annotated and simplified for readability.

License: MIT

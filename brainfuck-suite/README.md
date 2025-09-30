# Brainfuck Computational Suite

[![CI](https://github.com/iVGeek/BrainFuck-Computational-Suite/actions/workflows/python-tests.yml/badge.svg)](https://github.com/iVGeek/BrainFuck-Computational-Suite/actions/workflows/python-tests.yml)

An educational collection of Brainfuck programs and a tiny Python interpreter used to run and test them.

What you'll find
- `run_bf.py` — a minimal, tested Brainfuck interpreter (CLI + API)
- `modules/` — Brainfuck programs (Hello World, Fibonacci, Multiplication, I/O, simple utilities)
- `tests/` — pytest-based tests exercising the interpreter and deterministic modules
- `.github/workflows/` — CI workflow running tests, lint, black check, and mypy

Quick start
1. Run Hello World (from repository root):

```powershell
python .\brainfuck-suite\run_bf.py .\brainfuck-suite\modules\hello_world.bf
```

2. Run a deterministic multiplication example:

```powershell
python .\brainfuck-suite\run_bf.py .\brainfuck-suite\modules\multiplication_exact.bf
```

3. Run tests locally:

```powershell
python -m pytest -q
```

Using input
- To provide a string input: pass it as the second argument.
- To pipe raw bytes or read stdin: pass `-` as input or pipe into the command.

Examples (PowerShell):

```powershell
# Run Caesar shift (interactive/pass string)
python .\brainfuck-suite\run_bf.py .\brainfuck-suite\modules\caesar_exact.bf "A"

# Pipe binary input (write two bytes and pipe to calculator_add)
[System.IO.File]::WriteAllBytes('in.bin', (,[byte]4 + [byte]5)) ; Get-Content -Encoding Byte in.bin | python .\brainfuck-suite\run_bf.py .\brainfuck-suite\modules\calculator_add.bf

# Quick helper that runs non-interactive modules
.\brainfuck-suite\run_all.ps1
```

Interpreter features
- Supports Brainfuck commands: `+ - < > [ ] . ,`
- Configurable tape size: `--cells`
- Configurable cell width: `--cell-bits` (default 8)
- Toggle wrapping on overflow: `--no-wrap`
- Configurable maximum step count: `--max-steps`

Developer setup
1. (Optional) Create and activate a Python virtual environment.
2. Install dev dependencies:

```powershell
python -m pip install -U pip
pip install -r requirements-dev.txt
# or install tools individually: pip install pytest black flake8 mypy
```

CI
- The repository includes a GitHub Actions workflow at `.github/workflows/python-tests.yml`. It runs on pushes and PRs targeting `main` and performs:
  - pytest
  - flake8
  - black --check
  - mypy

Contributing
- Pull requests are welcome. Please run tests and lint locally before opening a PR.

License
- MIT

If you want, I can also add a `requirements-dev.txt`, contribution guidelines, or badges for code quality and coverage.

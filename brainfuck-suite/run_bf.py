"""Small Brainfuck interpreter with a simple CLI and API.

Usage:
    python run_bf.py modules/hello_world.bf

It supports ',' input from stdin, '.' output to stdout, and basic BF commands + - < > [ ]
"""
import sys
import argparse
from typing import List


def run_brainfuck(code: str, inp: bytes = b"", cells: int = 30000, max_steps: int = 10_000_000, cell_bits: int = 8, wrap: bool = True) -> (bytes, str):
    """Run Brainfuck code.

    Returns a tuple (output_bytes, debug_str)
    """
    tape = [0] * cells
    ptr = 0
    pc = 0
    input_ptr = 0
    output_bytes = bytearray()
    code_len = len(code)

    # Precompute matching brackets
    stack = []
    bracket_map = {}
    for i, c in enumerate(code):
        if c == "[":
            stack.append(i)
        elif c == "]":
            if not stack:
                raise SyntaxError(f"Unmatched ']' at position {i}")
            j = stack.pop()
            bracket_map[i] = j
            bracket_map[j] = i
    if stack:
        raise SyntaxError(f"Unmatched '[' at position {stack[-1]}")

    steps = 0
    while pc < code_len:
        if steps > max_steps:
            raise RuntimeError("Max steps exceeded")
        steps += 1
        cmd = code[pc]
        if cmd == ">":
            ptr += 1
            if ptr >= cells:
                raise MemoryError("Pointer moved beyond tape size")
        elif cmd == "<":
            ptr -= 1
            if ptr < 0:
                raise MemoryError("Pointer moved before start of tape")
        elif cmd == "+":
            val = tape[ptr] + 1
            if wrap:
                mask = (1 << cell_bits) - 1
                tape[ptr] = val & mask
            else:
                tape[ptr] = val
        elif cmd == "-":
            val = tape[ptr] - 1
            if wrap:
                mask = (1 << cell_bits) - 1
                tape[ptr] = val & mask
            else:
                tape[ptr] = val
        elif cmd == ".":
            output_bytes.append(tape[ptr])
        elif cmd == ",":
            if input_ptr < len(inp):
                tape[ptr] = inp[input_ptr]
                input_ptr += 1
            else:
                tape[ptr] = 0
        elif cmd == "[":
            if tape[ptr] == 0:
                pc = bracket_map[pc]
        elif cmd == "]":
            if tape[ptr] != 0:
                pc = bracket_map[pc]
        pc += 1

    debug = f"steps={steps} ptr={ptr} cells_used={sum(1 for v in tape if v!=0)}"
    return bytes(output_bytes), debug


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a Brainfuck (.bf) file")
    parser.add_argument("path", help="Path to .bf file")
    parser.add_argument("input", nargs="?", help="Input string or '-' to read raw stdin bytes")
    parser.add_argument("--cells", type=int, default=30000, help="Number of tape cells (default: 30000)")
    parser.add_argument("--max-steps", type=int, default=10_000_000, help="Maximum execution steps before aborting")
    parser.add_argument("--cell-bits", type=int, default=8, help="Bits per cell (default: 8)")
    parser.add_argument("--no-wrap", action="store_true", help="Disable wrapping on cell overflow/underflow")
    args = parser.parse_args()

    if args.input == "-":
        user_input = sys.stdin.buffer.read()
    elif args.input is None:
        # If stdin is not a TTY and has data, read raw bytes
        try:
            if not sys.stdin.isatty():
                user_input = sys.stdin.buffer.read()
            else:
                user_input = b""
        except Exception:
            user_input = b""
    else:
        user_input = args.input.encode("utf-8")

    with open(args.path, "r", encoding="utf-8") as f:
        code = f.read()
    out, dbg = run_brainfuck(code, inp=user_input, cells=args.cells, max_steps=args.max_steps, cell_bits=args.cell_bits, wrap=(not args.no_wrap))
    sys.stdout.buffer.write(out)
    sys.stdout.write("\n" + dbg + "\n")

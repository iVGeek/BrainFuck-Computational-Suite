import os
import importlib.util


def _load_run_bf_module():
    here = os.path.dirname(__file__)
    base = os.path.normpath(os.path.join(here, '..'))
    run_bf_path = os.path.join(base, 'run_bf.py')
    spec = importlib.util.spec_from_file_location('run_bf', run_bf_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_hello_world_output():
    here = os.path.dirname(__file__)
    bf_path = os.path.join(here, '..', 'modules', 'hello_world.bf')
    bf_path = os.path.normpath(bf_path)
    with open(bf_path, 'r', encoding='utf-8') as f:
        code = f.read()
    run_bf = _load_run_bf_module()
    out, dbg = run_bf.run_brainfuck(code)
    # Should produce some output bytes
    assert isinstance(out, (bytes, bytearray))
    assert len(out) > 0


def test_multiplication_exact():
    import importlib.util, os
    here = os.path.dirname(__file__)
    bf_path = os.path.normpath(os.path.join(here, '..', 'modules', 'multiplication_exact.bf'))
    with open(bf_path, 'r', encoding='utf-8') as f:
        code = f.read()
    run_bf = _load_run_bf_module()
    out, dbg = run_bf.run_brainfuck(code)
    # Should output a single byte equal to 30
    assert isinstance(out, (bytes, bytearray))
    assert len(out) == 1
    assert out[0] == 30


def test_fibonacci_exact():
    import os
    here = os.path.dirname(__file__)
    bf_path = os.path.normpath(os.path.join(here, '..', 'modules', 'fibonacci_exact.bf'))
    with open(bf_path, 'r', encoding='utf-8') as f:
        code = f.read()
    run_bf = _load_run_bf_module()
    out, dbg = run_bf.run_brainfuck(code)
    # Expecting 6 bytes: 0,1,1,2,3,5
    assert list(out[:6]) == [0, 1, 1, 2, 3, 5]


def test_char_io_exact():
    import os
    here = os.path.dirname(__file__)
    bf_path = os.path.normpath(os.path.join(here, '..', 'modules', 'char_io_exact.bf'))
    with open(bf_path, 'r', encoding='utf-8') as f:
        code = f.read()
    run_bf = _load_run_bf_module()
    inp = bytes([65, 66])
    out, dbg = run_bf.run_brainfuck(code, inp=inp)
    assert out == inp


def test_caesar_exact():
    import os
    here = os.path.dirname(__file__)
    bf_path = os.path.normpath(os.path.join(here, '..', 'modules', 'caesar_exact.bf'))
    with open(bf_path, 'r', encoding='utf-8') as f:
        code = f.read()
    run_bf = _load_run_bf_module()
    inp = bytes([65])  # 'A' -> 'D'
    out, dbg = run_bf.run_brainfuck(code, inp=inp)
    assert out == bytes([68])

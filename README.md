# PCPC (Python CFFI Performance Comparison)

The purpose of this repo is to compare different options for creating Python modules and their efficiency, relative to each-other.

# TODOs
- *Add more benchmarks*
- *Add Cython and possibly numba.jit versions of benchmarks*

# How Libraries Were Built
- **Nuitka** -- `nuitka3 --lto --module /path/to/lib.py`
- **Nim** -- `nim c --app:lib -d:release --out:lib.[so|pyd] /path/to/lib.nim`

# Current Benchmark Output
```console
# ./benchmark_all.sh

Running benchmark 'fibonacci_iterative' to 100000 places.
---------------------------------------------------------
Pure Python : 1.7613s
Nuitka      : 1.8141s                                    0.97x
Nim         : 0.0007s                                2,619.10x

Running benchmark 'fibonacci_recursive' to 30 places.
-----------------------------------------------------
Pure Python : 2.4137s
Nuitka      : 1.6588s                                    1.46x
Nim         : 0.0275s                                   87.93x
```

# Suggestions
Suggestions for more benchmarks are welcome, as well as PRs.
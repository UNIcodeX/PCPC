# PCPC (Python CFFI Performance Comparison)

The purpose of this repo is to compare different options for creating Python modules and their efficiency, relative to each-other.

# TODOs
- *Add more benchmarks*
- *Add numba.jit versions of benchmarks*

# How Libraries Were Built
- **Nuitka** -- `nuitka3 --lto --module /path/to/lib.py`
- **Cython** -- `cythonize -a -i /path/to/lib.pyx`
- **Nim** -- `nim c --app:lib -d:release --out:lib.[so|pyd] /path/to/lib.nim`

# Current Benchmark Output
```console
$ ./benchmark_all.sh 

Running benchmark 'fibonacci_iterative' to 100000 places.
---------------------------------------------------------
Pure Python : 2.6756s
Nuitka      : 2.6841s                                    1.00x
Cython      : 0.0015s                                1,795.20x
Nim         : 0.0008s                                3,294.82x

Running benchmark 'fibonacci_recursive' to 30 places.
-----------------------------------------------------
Pure Python : 3.5730s
Nuitka      : 2.3132s                                    1.54x
Cython      : 0.6638s                                    5.38x
Nim         : 0.0372s                                   96.17x
```

# Suggestions
Suggestions for more benchmarks are welcome, as well as PRs.
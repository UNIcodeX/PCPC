# PCPC (Python CFFI Performance Comparison)

The purpose of this repo is to compare different options for creating Python modules and their efficiency, relative to each-other.

# TODOs
- *Add more benchmarks*

# How Libraries Were Built
- **Nuitka** -- `nuitka3 --lto --module /path/to/lib.py`
- **Cython** -- `cythonize -a -i /path/to/lib.pyx`
- **Nim** -- `nim c --app:lib -d:release --gc:markAndSweep --out:lib.[so|pyd] /path/to/lib.nim`

# Current Benchmark Output
```console
$ ./benchmark_all.sh 

Running benchmark 'fibonacci_iterative' to 100000 places.
---------------------------------------------------------
Python : 0.8965s                                    1.00x
Nuitka : 0.9262s                                    0.97x
Cython : 0.0005s                                1,739.70x
Numba  : 0.0004s                                2,287.39x
Nim    : 0.0003s                                2,903.84x

Running benchmark 'fibonacci_recursive' to 30 places.
---------------------------------------------------------
Python : 1.2584s                                    1.00x
Nuitka : 0.8297s                                    1.52x
Cython : 0.2503s                                    5.03x
Numba  : 0.0373s                                   33.75x
Nim    : 0.0137s                                   92.06x

Running benchmark 'json_loads'.
_NOTE:_ JSON parsing within Nim is quite fast. I believe
there is extra overhead from converting each value to a
string. There is probably also more efficient way to do 
pass this data back to Python. Suggestions welcome.
---------------------------------------------------------
Python : 0.1633s                                    1.00x
Nuitka : 0.1583s                                    1.03x
Cython : 0.1573s                                    1.04x
Numba  : 0.5923s                                    0.28x
Nim    : 0.5128s                                    0.32x

Running benchmark 'gen_range'.
---------------------------------------------------------
Python : 0.4937s                                    1.00x
Nuitka : 0.4567s                                    1.08x
Cython : 0.1428s                                    3.46x
Numba  : 0.3121s                                    1.58x
Nim    : 0.3362s                                    1.47x
```

Benchmarks were ran in a VM with the following specs.
```
 OS: Antergos 
 Kernel: x86_64 Linux 
 Packages: 908
 Shell: zsh 5.7.1
 CPU: Intel Core i7-6700 
 GPU: vboxdrmfb
 RAM: 1115MiB / 3000MiB
```

# Suggestions
Suggestions for more benchmarks are welcome, as well as PRs.

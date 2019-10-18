# PCPC (Python CFFI Performance Comparison)

The purpose of this repo is to compare different options for creating Python modules and their efficiency, relative to each-other.

![](https://img.shields.io/github/languages/top/UNIcodeX/PCPC?style=for-the-badge)
![](https://img.shields.io/github/languages/count/UNIcodeX/PCPC?logoColor=green&style=for-the-badge)
![](https://img.shields.io/github/stars/UNIcodeX/PCPC?style=for-the-badge "Star PCPC on GitHub!")
![](https://img.shields.io/maintenance/yes/2019?style=for-the-badge "2019")
![](https://img.shields.io/github/languages/code-size/UNIcodeX/PCPC?style=for-the-badge)
![](https://img.shields.io/github/issues-raw/UNIcodeX/PCPC?style=for-the-badge "Bugs")
![](https://img.shields.io/github/issues-pr-raw/UNIcodeX/PCPC?style=for-the-badge "PRs")
![](https://img.shields.io/github/last-commit/UNIcodeX/PCPC?style=for-the-badge "Commits")

# TODOs
- *Add more benchmarks*

# How Libraries Were Built
- **Nuitka** -- `nuitka3 --lto --module /path/to/lib.py`
- **Cython** -- `cythonize -a -i /path/to/lib.pyx`
- **Nim** -- `nim c --app:lib -d:release --gc:markAndSweep --out:lib.[so|pyd] /path/to/lib.nim`
- **V** -- `v -shared -prod /path/to/lib.v`

# Current Benchmark Output
```console
$ ./benchmark_all.sh 

Running benchmark 'fibonacci_iterative' to 100000 places.
---------------------------------------------------------
Python : 1.1194s                                    1.00x
Nuitka : 1.1471s                                    0.98x
Cython : 0.0007s                                1,559.35x
Numba  : 0.0004s                                2,980.38x
Nim    : 0.0007s                                1,499.98x
V      : 0.0029s                                  383.67x

Running benchmark 'fibonacci_recursive' to 30 places.
---------------------------------------------------------
Python : 1.6359s                                    1.00x
Nuitka : 1.0064s                                    1.63x
Cython : 0.3227s                                    5.07x
Numba  : 0.0582s                                   28.13x
Nim    : 0.0182s                                   89.79x
V      : 0.0585s                                   27.97x

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

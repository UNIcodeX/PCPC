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
Python : 1.7121s                                    1.00x
Nuitka : 1.7981s                                    0.95x
Cython : 0.0011s                                1,593.43x
Numba  : 0.0009s                                1,938.55x
Nim    : 0.0006s                                2,942.66x

Running benchmark 'fibonacci_iterative' to 30 places.
---------------------------------------------------------
Python : 2.3615s                                    1.00x
Nuitka : 1.6276s                                    1.45x
Cython : 0.5165s                                    4.57x
Numba  : 0.0728s                                   32.42x
Nim    : 0.0274s                                   86.06x

Running benchmark 'json_loads'.
---------------------------------------------------------
Python : 0.8010s                                    1.00x
Nuitka : 0.7802s                                    1.03x
Cython : 0.7711s                                    1.04x
Numba  : 1.8025s                                    0.44x
Nim    : 4.0788s                                    0.20x

Running benchmark 'gen_range'.
---------------------------------------------------------
Python : 2.3825s                                    1.00x
Nuitka : 2.1886s                                    1.09x
Cython : 0.6802s                                    3.50x
Numba  : 1.4858s                                    1.60x
Nim    : 1.6071s                                    1.48x
```

Benchmarks were ran in a VM with the following specs.
```
               `.-/::/-``                
            .-/osssssssso/.               j@A1
           :osyysssssssyyys+-             OS: Antergos 
        `.+yyyysssssssssyyyyy+.           Kernel: x86_64 Linux 5.0.0-arch1-1-ARCH
       `/syyyyyssssssssssyyyyys-`         Uptime: 2d 16h 50m
      `/yhyyyyysss++ssosyyyyhhy/`         Packages: 908
     .ohhhyyyyso++/+oso+syy+shhhho.       Shell: zsh 5.7.1
    .shhhhysoo++//+sss+++yyy+shhhhs.      Resolution: 1768x1492
   -yhhhhs+++++++ossso+++yyys+ohhddy:     DE: Budgie
  -yddhhyo+++++osyyss++++yyyyooyhdddy-    WM: BudgieWM
 .yddddhso++osyyyyys+++++yyhhsoshddddy`   WM Theme: Numix-Frost-Light
`odddddhyosyhyyyyyy++++++yhhhyosddddddo   GTK Theme: Adwaita-dark [GTK2/3]
.dmdddddhhhhhhhyyyo+++++shhhhhohddddmmh.  Icon Theme: Numix-Square
ddmmdddddhhhhhhhso++++++yhhhhhhdddddmmdy  Font: Fira Code 11
dmmmdddddddhhhyso++++++shhhhhddddddmmmmh  CPU: Intel Core i7-6700 @ 2x 3.408GHz
-dmmmdddddddhhyso++++oshhhhdddddddmmmmd-  GPU: vboxdrmfb
 .smmmmddddddddhhhhhhhhhdddddddddmmmms.   RAM: 1115MiB / 3000MiB
   `+ydmmmdddddddddddddddddddmmmmdy/.    
      `.:+ooyyddddddddddddyyso+:.`       

```

# Suggestions
Suggestions for more benchmarks are welcome, as well as PRs.
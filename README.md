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
Pure Python : 1.8041s
Nuitka      : 1.8607s                                    0.97x
Cython      : 0.0010s                                1,737.52x
Numba       : 0.0009s                                2,111.11x
Nim         : 0.0007s                                2,721.75x

Running benchmark 'fibonacci_recursive' to 30 places.
-----------------------------------------------------
Pure Python : 2.6576s
Nuitka      : 1.9326s                                    1.38x
Cython      : 0.5002s                                    5.31x
Numba       : 0.0748s                                   35.51x
Nim         : 0.0278s                                   95.71x
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
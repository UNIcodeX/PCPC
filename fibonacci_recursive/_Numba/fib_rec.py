from numba import jit, int64

@jit(int64(int64,))
def fibRec(n):
    if n <= 2:
        return 1
    else:
        return fibRec(n-1) + fibRec(n-2)

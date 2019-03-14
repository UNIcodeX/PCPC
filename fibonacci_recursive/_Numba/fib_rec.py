from numba import jit, int32, int64

@jit(int32(int32,))
def fibRec(n):
    if n <= 2:
        return 1
    else:
        return fibRec(n-1) + fibRec(n-2)

def fibRec(int n):
    if n <= 2:
        return 1
    else:
        return fibRec(n-1) + fibRec(n-2)

def f(n):
    if (n<1):
        return 1
    else:
        return n*f(n-1)*f(n-2)
print(f(4))

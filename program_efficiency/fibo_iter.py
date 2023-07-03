def fibo(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        t1 = 0
        t2 = 1
        for i in range(n-1):
            # (t1, t2) = (t2, t1+t2)
            temp = t1
            t1 = t2
            t2 = temp+t2
    return t2


print(fibo(4))

# for i in range(10):
#     print(fibo(i))

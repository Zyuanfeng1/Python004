def map(func,*args,**kargs):
    return func(*args,**kargs)
def fun(k):
    return k+9

print(map(fun,9))
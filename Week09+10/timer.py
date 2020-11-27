import time

def timer(func,*args,**kargs):
    def inner(*args,**kwargs):
        start=time.time()
        ret=func(*args,**kargs)
        print('running time: ',time.time()-start,'\nstart: ',start,'\nfinish: ',time.time())
        return ret
    return inner

@timer
def fun(a,b,c):
    return a+b+c

print(fun(1,2,4))


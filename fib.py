def fib(n):
    c,p  = 1,0
    if n < 2:
       return n 
    while(n > 1):
    	c ,p = c+p, c
        n -= 1
    return c

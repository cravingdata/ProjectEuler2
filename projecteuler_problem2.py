def fibonacci1(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci1(n-1) + fibonacci1(n-2)

def fibonacci2(p):
    a,b = 1,1
    for i in range(p-1):
        a, b = b, a+b
    return a

def fibonacci3(n):
    a,b = 1, 2
    for i in range(n-1):
        a,b = b, a+b
    return a
print 6 * 4 + 3

class = "computer science"

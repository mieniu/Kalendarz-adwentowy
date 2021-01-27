import time

SIX = 6**4

def f(n):
    a, b = 0, 1
    for i in range(0, n):
        a, b = b, (a + b)%SIX
    
    return a

def to_base(n, b):
    res = []
    while n>0:
        res.append(str(n%b))
        n //= b
    res.reverse()
    return "".join(res)

start = time.time()
print(to_base(f(1234567890), 6))
stop = time.time()
print(f"Operacja zajęła {stop-start} sekund.")
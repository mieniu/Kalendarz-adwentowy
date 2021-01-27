n = 235890082423
e = 65537
c = 97303533918

for i in range(2, n//2+1):
    if n%i == 0:
        p = i
        q = n//i
        break

fi = (p-1)*(q-1)


def nwd(a, b):
    while b != 0:
        c = a%b
        a = b
        b = c
    return a

print(f"p={p}")
print(f"q={q}")
print(f"fi={fi}")
print(f"e={e}")

# tu wychodzi 235_039_425_257
d = 235039425257
# d = fi 
# while (d*e)%fi != 1:własności modulo
#     d -= 1
# print(f"d={d}")

def power(x, y, p) : 
    res = 1     # Initialize result 
  
    # Update x if it is more 
    # than or equal to p 
    x = x % p  
      
    if (x == 0) : 
        return 0
  
    while (y > 0) : 
          
        # If y is odd, multiply 
        # x with result 
        if ((y & 1) == 1) : 
            res = (res * x) % p 
  
        # y must be even now 
        y = y >> 1      # y = y/2 
        x = (x * x) % p 
          
    return res 

def power2(a, b, c):
    res = a
    while b > 1:
        res = (res*a)%c
        b -= 1
    return res

m = power(c, d, n)
print(m)


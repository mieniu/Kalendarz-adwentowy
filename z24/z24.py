# tutaj zrobiłem przez C++ (ZNAJDŹ TEN KOD NA KOMPUTERZE)

def is_primary(n):
    i = 2
    if n<2:
        return False
    while i**2 <= n:
        if n%i == 0:
            return False
        i += 1
    return True

def properDivisorSum(n): 
    sum = 0
  
    # Loop to iterate over all the 
    # numbers from 1 to N 
    for i in range(n+1): 
  
        # Find all divisors of 
        # i and add them 
        for j in range(1, i + 1): 
            if j * j > i: 
                break
            if (i % j == 0): 
                if (i // j == j): 
                    sum += j 
                else: 
                    sum += j + i // j 
  
        # Subtracting 'i' so that the 
        # number itself is not included 
        sum = sum - i 
  
    return sum

def has_dividers_8_multiplication(n):
    sum = 1
    i = 2
    while i*i < n:
        if n%i == 0:
            sum += i + n//i
            print(i)
            print(n//i)
        i += 1

    if n%i == 0:
        print(i)
        sum += i

    print(sum)
    
    if sum%8 == 0:
        return True
    return False

def get_answer(n):
    ctr = 0
    for i in range(2, n+1):
        temp = properDivisorSum(i)
        if temp % 8 == 0:
            ctr += 1
        if i%10_000 == 0:
            print(i, ctr)
    return ctr

import time
start = time.time()
# print(get_answer(200_000))
print(has_dividers_8_multiplication(20))
stop = time.time()
print(f"Czas: {stop-start}")
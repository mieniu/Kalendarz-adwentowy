def compare(a,b):
    for base in range(10,1,-1):
        s_a = sum_digits_with_base(a, base)
        s_b = sum_digits_with_base(b, base)
        if s_b > s_a:
            return b
        if s_a > s_b:
            return a
    return a

def sum_digits_with_base(a, base=10):
    s = 0
    while a > 0:
        s += a%base
        a //= base
    return s

if __name__ == "__main__":
    with open('porzadek.in') as f:
        nums = [int(i) for i in f.read().split()]
        
    maximum = 1000
    for i in nums: 
        maximum = compare(maximum, i)
    print(maximum)
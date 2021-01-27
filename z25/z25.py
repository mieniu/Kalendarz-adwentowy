WEIGHTS = [1,3,7,9,1,3,7,9,1,3]
def control_digit(n):
    digits = [int(i) for i in n]
    control = 0
    for i in zip(digits, WEIGHTS):
        control += (i[0]*i[1])%10
    return 10-(control%10)

def how_many_with_control_digit(n=5):
    ctr = 0
    for i in pesels:
        if control_digit(i) == n:
            ctr += 1
    return ctr

with open('pesele.in') as f:
    pesels = f.read().split()
print(how_many_with_control_digit())
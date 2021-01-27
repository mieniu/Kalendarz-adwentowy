with open('licznik.in') as f:
    numbers = [int(i) for i in f.readlines()]

def bin_table(n):
    res = []
    ops = 0
    while(n > 0):
        ops += 1
        res.insert(0, n%2)
        n //= 2
    for _ in range(32-ops):
        res.insert(0, 0)
    return res


def how_many_flips(a, b):
    ctr = 0
    for i in zip(a,b):
        if i[0] != i[1]:
            ctr += 1
    return ctr


current = 0
all_flips = 0
for i in numbers:
    next_val = current + i
    bin_next = bin_table(next_val)
    bin_current = bin_table(current)

    rotated = how_many_flips(bin_next, bin_current)
    all_flips += rotated
    print(f"Dodajemy {i}")
    print(f"{next_val} => {bin_next}")
    print(f"{current} => {bin_current}")
    print("Obrócono:",rotated )
    print("Wszystkich obróceń:", all_flips)
    print('-------')
    current = next_val
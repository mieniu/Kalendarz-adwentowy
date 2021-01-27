def is_primary(n):
    i = 2
    if n<2:
        return False
    while i**2 <= n:
        if n%i == 0:
            return False
        i += 1
    return True

with open('primaries.txt', 'w+') as f:
    for i in range(2, 2100):
        if is_primary(i):
            f.write(f"{i}\n")
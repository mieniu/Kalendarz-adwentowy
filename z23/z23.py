import time

def get_how_many_goldbach_combinations(limit):
    with open('primaries.txt') as f:
        primaries = [int(i) for i in f.readlines()]

    ctr = 0
    for n in range(7, limit, 2):
        i = 0
        while primaries[i] <= n:
            j = i
            while primaries[j] <= n - primaries[i]:
                k = j
                while primaries[k] <= n-primaries[i]-primaries[j]:
                    if primaries[i] + primaries[j] + primaries[k] == n:
                        ctr += 1
                        break
                    else:
                        k += 1
                j += 1
            i += 1

    return ctr

start = time.time()
print(f"Wynik: {get_how_many_goldbach_combinations(2020)}")
stop = time.time()
print(f"Czas: {stop-start}")
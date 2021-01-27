import time

def sum(n):
    start = time.time()
    r = 0
    for i in range(n):
        r += 2
    stop = time.time()
    print("Calost zajela: " + str(stop-start) + " sekund.")
    return r

sum(1000000)
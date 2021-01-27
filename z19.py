import time
x0 = 21380413
x1 = 32564732
x2 = 803330610
m = 928377461

def get_c(A):
    return x1 - (A*x0)%m

def get_random_number(a, c, x):
    return (a*x + c)%m

def get_x3():
    start = time.time()
    for a in range(928377461):
        c = get_c(a)
        if x2 == get_random_number(a, c, x1):
            break
    stop = time.time()
    print(f"Operacja zajęła {stop-start} sekund.\n"
          f"a={a}\n"
          f"c={c}\n"
          f"x3={get_random_number(a, c, x2)}")

get_x3()
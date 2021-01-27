def to_dec(arr, b):
    res = 0
    temp = 1
    for i in reversed(arr):
        res += i*temp
        temp *= b
    return res

t = [1, 2, 3, 4]
res = sum([to_dec(t, i) for i in range(5, 2021)])

print(res)
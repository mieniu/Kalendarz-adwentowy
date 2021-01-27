with open('podciąg.in') as f:
    res = [int(i) for i in f.readlines()]

max_length = 1
max_start = res[0]
temp = 1
temp_start = res[0]

for i in range(1,10000):
    if res[i] > res[i-1]:
        temp += 1
    else:
        if temp > max_length:
            max_length = temp
            max_start = temp_start
        temp = 1
        temp_start = res[i]

if temp > max_length:
    max_length = temp
    max_start = temp_start

print(max_length)
print(max_start)
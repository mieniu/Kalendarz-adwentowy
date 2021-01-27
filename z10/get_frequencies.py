words = []
with open("szyfrogram.in") as f:
    temp = f.read().split()
words = "".join(temp)

frequencies = {}

for i in words:
    if i in frequencies.keys():
        frequencies[i] += 1
    else:
        frequencies[i] = 1

sum_of_all_chars = 0
for i in frequencies.values():
    sum_of_all_chars += i

for i in frequencies.keys():
    frequencies[i] = round(frequencies[i] / sum_of_all_chars * 100, 3)

frequencies = sorted(frequencies.items(), key = lambda x: x[1], reverse = True)

with open("z10_frequencies.out", "w+") as f:
    for i in frequencies:
        f.write(f"{i[0]} {i[1]}\n")
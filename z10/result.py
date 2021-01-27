with open("z10_text.out") as f:
    text = f.read()

sum = 0
for i in text:
    if i in 'ACFGJLOUWZ':
        sum += 1

print(sum)
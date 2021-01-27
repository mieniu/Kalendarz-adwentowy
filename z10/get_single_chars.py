with open("szyfrogram.in") as f:
    words = f.read().split()
    
res = set()
for i in words:
    print(len(i))
    if len(i) == 1:
        res.add(i)

print(res)
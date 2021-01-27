with open("zamowienia.in") as f:
    orders = [int(i) for i in f.readlines()]

orders_in_time = [0 for _ in range(503)]

for i in orders:
    orders_in_time[i-1] += 1
    orders_in_time[i] += 1
    orders_in_time[i+1] += 1

print(max(orders_in_time))
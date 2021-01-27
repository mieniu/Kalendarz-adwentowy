if __name__ == "__main__":
    with open("zamowienia.in") as f:
        orders = [int(i) for i in f.read().split()]

    orders_in_time = [0 for _ in range(501)]
    for i in orders:
        orders_in_time[i] += 1

    print(max(orders_in_time))
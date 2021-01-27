# najdłuższy czas to 5076
# największy priorytet to 96
# wynik nie moży być większy niż 48729600
# obecnie najmniej: 5570461

def create_pair(vals) -> dict:
    return {
        'needed_time': vals[0],
        'priority':    vals[1],
        'ratio':       round(vals[0] / vals[1], 5),
        'sum_time':    vals[0],
    }

with open('prezenty.in') as f:
    data = [int(i) for i in f.read().split()]

pairs = [create_pair(vals) for vals in zip(data[0::2], data[1::2])]


# -------------
# Tutaj wynik wychodzi: 5570461
# ------------
pairs = sorted(pairs, key = lambda i: i["ratio"], reverse = False)

how_many = len(pairs)
sum = 0
for _ in range(how_many):
    sum += pairs[0]['sum_time'] * pairs[0]['priority']
    time = pairs[0]['needed_time']
    pairs.pop(0)
    for i, val in enumerate(pairs):
        pairs[i]['sum_time'] += time

print(sum)

# --------------
# a tu jeszcze gorzej: 6538428
# --------------
# how_many = len(pairs)
# sum = 0
# for _ in range(how_many):
#     for i in range(len(pairs)):
#         pairs[i]['ratio'] = pairs[i]['sum_time']/pairs[i]['priority']
    
#     pairs = sorted(pairs, key = lambda i: i['ratio'], reverse = False)

#     sum += pairs[0]['sum_time'] * pairs[0]['priority']
#     time = pairs[0]['needed_time']
#     pairs.pop(0)
#     for i in range(len(pairs)):
#         pairs[i]['sum_time'] += time
#
# print(sum)
# --------------
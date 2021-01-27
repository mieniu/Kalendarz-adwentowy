class Vertice:
    counter = 0

    def __init__(self, value, 
                 top, top_cost, 
                 right, right_cost, 
                 bottom, bottom_cost, 
                 left, left_cost):
        self.top = top
        self.right = right
        self.bottom = bottom
        self.left = left
        self.top_cost = top_cost
        self.right_cost = right_cost
        self.bottom_cost = bottom_cost
        self.left_cost = left_cost
        self.id = Vertice.counter
        self.value = value
        Vertice.counter += 1
    
    def __str__(self):
        return(f"ID: {self.id}"
               f"Value: {self.value}"
               f"Top: {self.top} {self.top_cost}"
               f"Right: {self.right} {self.right_cost}"
               f"Bottom: {self.bottom} {self.bottom_cost}"
               f"Left: {self.left} {self.left_cost}")

def get_vertices(points):
    vertices = []
    for i in range(100):
        for j in range(100):
            top = None
            top_cost = None
            bottom_cost = None
            bottom = None
            left = None
            left_cost = None
            right = None
            right_cost = None
            if i != 0:
                top_cost = points[i-1][j]
                top = 100*i+j - 100
            if i != 99:
                bottom_cost = points[i+1][j]
                bottom = 100*i+j + 100
            if j != 0:
                left_cost = points[i][j-1]
                left = 100*i+j-1
            if j != 99:
                right_cost = points[i][j+1]
                right = 100*i+j+1
            vertices.append([Vertice(points[i][j], top, top_cost, right, right_cost, bottom, bottom_cost, left, left_cost), False])
    return vertices

def get_min_from_d(q, d):
    min_i = 0
    while q[min_i][1] == True:
        min_i += 1

    for i in range(len(d)):
        if q[i][1] == False:
            if d[i] < d[min_i]:
                min_i = i
    return min_i

with open('plansza.in') as f:
    temp = [int(i) for i in f.read().split()]

points = []
for i in range(100):
    row = [temp[i*100+j] for j in range(100)]
    points.append(row)
del temp

q = get_vertices(points)
d = [float('inf') for _ in q]
d[0] = 0
p = [-1 for _ in q]

for a in range(10000):
    u = get_min_from_d(q, d)
    q[u][1] = True

    # top
    if q[u][0].top != None:
        w = q[u][0].top
        if q[w][1] == False:
            if d[w] > d[u] + q[u][0].top_cost:
                d[w] = d[u] + q[u][0].top_cost
                p[w] = u

    # right
    if q[u][0].right != None:
        w = q[u][0].right
        if q[w][1] == False:
            if d[w] > d[u] + q[u][0].right_cost:
                d[w] = d[u] + q[u][0].right_cost
                p[w] = u

    # bottom
    if q[u][0].bottom != None:
        w = q[u][0].bottom
        if q[w][1] == False:
            if d[w] > d[u] + q[u][0].bottom_cost:
                d[w] = d[u] + q[u][0].bottom_cost
                p[w] = u

    # left
    if q[u][0].left != None:
        w = q[u][0].left
        if q[w][1] == False:
            if d[w] > d[u] + q[u][0].left_cost:
                d[w] = d[u] + q[u][0].left_cost
                p[w] = u

    print(a)

with open('res.txt', 'w+') as f:
    for i, val in enumerate(zip(p, d)):
        f.write(f"W{i}: {val}\n")
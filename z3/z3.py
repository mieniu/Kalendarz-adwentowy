with open('punkty.in') as f:
    points = f.read().split()

points = [(int(i), int(j)) for i, j in zip(points[0::2], points[1::2])]

def dist(p1, p2):
    return (p1[0] - p2[0])**2 + (p1[1] - p1[1])**2

m_x = -200
m_y = -200
how_many = 0

for p in points:
    ctr = -1
    for p2 in points:
        if dist(p, p2) <= 30:
            ctr += 1
    
    if ctr > how_many:
        how_many = ctr
        m_x = p[0]
        m_y = p[1]

print(f"Ile punktów: {how_many}\n"
      f"Współrzędne: ({m_x}, {m_y})")
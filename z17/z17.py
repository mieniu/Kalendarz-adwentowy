with open('punkty.in') as f:
    arr = f.read().split()
points = []
for i in range(len(arr)//2):
    temp = dict()
    temp['x'] = int(arr[2*i])
    temp['y'] = int(arr[2*i+1])
    points.append(temp)


import math
def dist(p1, p2):
    return math.sqrt((p1['x']-p2['x'])**2 + (p1['y']-p2['y'])**2)


def how_many_points_in_circle(p):
    ctr = 0
    for j in range(2500):
        if dist(points[j], p) <= 30:
            ctr += 1
    if p in points:
        ctr -= 1
    return ctr


def get_coords(p1, p2):
    q = dist(p1,p2)
    if q <= 60 and q > 0:
        x3 = (p1['x'] + p2['x'])/2
        y3 = (p1['y'] + p2['y'])/2
        c = math.sqrt(900-(q/2)**2)
        x1 = x3 + c*(p1['y']-p2['y'])/q
        y1 = y3 + c*(p1['x']-p2['x'])/1
        x2 = x3 - c*(p1['y']-p2['y'])/q
        y2 = y3 - c*(p1['x']-p2['x'])/1
        return [
            {
                'x': x1,
                'y': y1,
            },
            {
                'x': x2,
                'y': y2,
            }]
    return None


def analize():
    for i in range(2500):
        points[i]['how_many'] = how_many_points_in_circle(points[i])


    points.sort(key=lambda x: x['how_many'], reverse=True)
    with open('points_analysis.txt', 'w+') as f:
        for p in points:
            f.write(f"({p['x']}; {p['y']}) -> {p['how_many']}\n")


def attempt2():
    maximum = 0
    for x in range(-200, 201):
        temp['x'] = x
        for y in range(-200, 201):
            temp['y'] = y
            temp_val = how_many_points_in_circle(temp)

            if temp_val > maximum:
                maximum = temp_val
    return maximum

def compare(a, b):
    if a > b:
        return a
    return b

def attempt3():
    maximum = 0
    for p1 in points:
        print(f"{p1}, maximum: {maximum}")
        for p2 in points:
            temp = get_coords(p1, p2)
            if (temp):
                maximum = compare(maximum, how_many_points_in_circle(temp[0]))
                maximum = compare(maximum, how_many_points_in_circle(temp[1]))
    return maximum
            
print(attempt3())
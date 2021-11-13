import math
import sys
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

def check_clockwise(polygon):
    s = 0
    counts = len(polygon)
    for i in range(counts):
        point = polygon[i]
        point2 = polygon[(i + 1) % counts]
        s += (point2.x - point.x) * (point2.y + point.y)
    return s > 0

def check_ear(p1, p2, p3, polygon):
    return Nopoints_check(p1, p2, p3, polygon) and check_convex(p1, p2, p3) and area_triangle(p1.x, p1.y, p2.x, p2.y, p3.x, p3.y) > 0

def Nopoints_check(p1, p2, p3, polygon):
    for pn in polygon:
        if pn in (p1, p2, p3):
            continue
        elif check_inside(pn, p1, p2, p3):
            return False
    return True

def check_inside(p, a, b, c):
    area = area_triangle(a.x, a.y, b.x, b.y, c.x, c.y)
    area1 = area_triangle(p.x, p.y, b.x, b.y, c.x, c.y)
    area2 = area_triangle(p.x, p.y, a.x, a.y, c.x, c.y)
    area3 = area_triangle(p.x, p.y, a.x, a.y, b.x, b.y)
    areadiff = abs(area - sum([area1, area2, area3])) < (math.sqrt(sys.float_info.epsilon))
    return areadiff

def area_triangle(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

def check_convex(prev, point, next):
    return sum_triangle(prev.x, prev.y, point.x, point.y, next.x, next.y) < 0

def sum_triangle(x1, y1, x2, y2, x3, y3):
    return x1 * (y3 - y2) + x2 * (y1 - y3) + x3 * (y2 - y1)

def Earclip(polygon):

    ear_vertex = []
    triangles = []

    polygon = [Point(*point) for point in polygon] 

    if check_clockwise(polygon):  # Make polygon anticlockwise
        polygon.reverse()

    counts = len(polygon)  # Find ear vertices and add to ear_vertex
    for i in range(counts):
        prev_point = polygon[i - 1]
        point = polygon[i]
        next_point = polygon[(i + 1) % counts]
        if check_ear(prev_point, point, next_point, polygon):
            ear_vertex.append(point)

    while ear_vertex and counts >= 3: 
        ear = ear_vertex.pop(0)
        i = polygon.index(ear)
        prev_index = i - 1
        prev_point = polygon[prev_index]
        next_index = (i + 1) % counts
        next_point = polygon[next_index]

        polygon.remove(ear) #Removing ear vertices from polygon
        counts -= 1
        triangles.append(((prev_point.x, prev_point.y), (ear.x, ear.y), (next_point.x, next_point.y)))
        if counts > 3:
            prev_prev_point = polygon[prev_index - 1]
            next_next_index = (i + 1) % counts
            next_next_point = polygon[next_next_index]

            matches = [
                (prev_prev_point, prev_point, next_point, polygon),
                (prev_point, next_point, next_next_point, polygon),
            ]
            for match in matches:
                q = match[1]
                if check_ear(*match):
                    if q not in ear_vertex:
                        ear_vertex.append(q)
                elif q in ear_vertex:
                    ear_vertex.remove(q)
    return triangles
from polygon_triangulate import *
from Graphcoloring import *


# Cartesian coordinates for the vertices of a CLOSED polygon, in either clockwise or counter-clockwise order
polygon = [(1,0) , (3,0) , (4,3) , (4,5) , (2,4) , (3,2) ] # n = 5

print(polygon) # the input

# Triangulate the polygon
triangles = Earclip(polygon) # Returns 2D list of triangle vertex coordinates

# Add ^those vertices to a dict, without repeating any, mapping each to a index from 0 to n-1,
vertices = {}
for x, y, z in triangles:
    if x not in vertices: vertices[x] = len(vertices)
    if y not in vertices: vertices[y] = len(vertices)
    if z not in vertices: vertices[z] = len(vertices)

# initialize adjacency matrix of the triangle mesh to zeroes
num_vertices = len(vertices)

adjacency_matrix = [[0 for i in range(num_vertices)] for j in range(num_vertices)]

# populate adjacency matrix
for x, y, z in triangles:
    adjacency_matrix[vertices.get(x)][vertices.get(y)] = 1 
    adjacency_matrix[vertices.get(x)][vertices.get(z)] = 1

    adjacency_matrix[vertices.get(y)][vertices.get(x)] = 1
    adjacency_matrix[vertices.get(y)][vertices.get(z)] = 1

    adjacency_matrix[vertices.get(z)][vertices.get(x)] = 1
    adjacency_matrix[vertices.get(z)][vertices.get(y)] = 1

print(triangles) #Outputs the cartesian coordinates of resulting triangles
print(vertices) #Outputs the vertices of resulting triangles
for x in adjacency_matrix: print(x) #Outputs the adjacency matrix of the vertices

# Tricolor the vertices
g = graph(num_vertices)
g.Graph = adjacency_matrix
colors = g.Check_graph_color(3) # returns array with colors, in the order of vertices as in the dict vertices

# map colors to vertices
colored_vertices = {}
n = 0
for i in vertices.keys():
    colored_vertices[i] = [colors[n]]
    n+=1

# count frequency of colors and store in dict
color_freq = {}
for i in colors:
    if i in color_freq: color_freq[i]+=1
    else: color_freq[i] = 1

# determine least frequent color
frequency = num_vertices
for i in color_freq.keys():
    if color_freq[i] < frequency: 
        frequency = color_freq[i]
        least_frequent_color = i

# output array with cartesian coordinates for camera placement
chosen_vertices = []
for i in colored_vertices.keys():
    if colored_vertices[i] == [least_frequent_color]: 
        chosen_vertices.append(i)
print(num_vertices)
print(chosen_vertices) # the output
class graph(): 
  
    def __init__(self, vertices): 
        self.Vertex = vertices 
        self.Graph = [[0 for column in range(vertices)] 
                              for row in range(vertices)] 
  
    # check  current color assignment for vertex v 
    def Check_color(self, v, colour, c): 
        for i in range(self.Vertex): 
            if self.Graph[v][i] == 1 and colour[i] == c: 
                return False
        return True
      
    # recursive function to solve coloring problem 
    def Graph_util(self, m, colour, v): 
        if v == self.Vertex: 
            return True
  
        for c in range(1, m+1): 
            if self.Check_color(v, colour, c) == True: 
                colour[v] = c 
                if self.Graph_util(m, colour, v+1) == True: 
                    return True
                colour[v] = 0
  
    def Check_graph_color(self, m): 
        colour = [0] * self.Vertex 
        if self.Graph_util(m, colour, 0) == False: 
            return False
  
        #answer
        color_array = []
        for c in colour: color_array.append(c)
        return color_array
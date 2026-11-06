class Vertex:
    def __init__(self,name):
        self.name= name
        self.neighbours = []

    def add_neighbours(self,neighbour):
        self.neighbours.append(neighbour)
class Graph: 
    def __init__(self):
        self.nodes = []

    def add_node(self,name):
        node = Vertex(name)
        self.nodes.append(node)
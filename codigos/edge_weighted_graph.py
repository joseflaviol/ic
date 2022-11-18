from edge import Edge

class EdgeWeightedGraph:

    def __init__(self, V, E, oriented = False):
        self.V = V 
        self.E = E 
        self.oriented = oriented
        self.edges = []
        self.adjacency_list = []
        for i in range(V):
            self.adjacency_list.append([])

    def addEdge(self, u, v, w):
        edge = Edge(u, v, w)
        self.edges.append(edge)
        self.adjacency_list[u].append(edge)
        if not self.oriented:
            self.adjacency_list[v].append(edge)
    
    def adj(self, u):
        return self.adjacency_list[u]

    def getEdges(self):
        return self.edges
class Graph:

    def __init__(self, oriented = False):
        self.V, self.E, self.oriented = None, None, oriented
    
    def setV(self, V):
        self.V = V
        self.adjacency_list = []
        for i in range(V):
            self.adjacency_list.append([]) 
        self.E = 0 
    
    def getV(self):
        return self.V 
    
    def getE(self):
        return self.E 

    def addEdge(self, u, v):
        self.adjacency_list[u].append(v)
        if not self.oriented:
            self.adjacency_list[v].append(u)
        self.E += 1
    
    def adj(self, u):
        return self.adjacency_list[u]
    
    def __str__(self):
        s = str(self.getV()) + " vertices, " + str(self.getE()) + " edges\n"

        for i in range(self.getV()):
            s += str(i) + ": "
            for v in self.adj(i):
                s += str(v) + " "
            s += "\n"
        
        return s

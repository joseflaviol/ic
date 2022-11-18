class Edge:

    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w   
    
    def __str__(self):
        return "%d %d %d" % (self.u, self.v, self.w)
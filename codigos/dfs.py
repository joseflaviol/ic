class DepthFirstSearch:

    def __init__(self, G, s):
        self.marked = [False] * G.getV()
        self.edgeTo = [None] * G.getV()
        self.depth = [None] * G.getV()
        self.npe = {}
        self.npe["node"] = []
        self.npe["depth"] = []
        self.depth[s] = 0
        self.dfs(G, s)

    def dfs(self, G, u):
        self.marked[u] = True 
        self.npe["node"].append(u)
        self.npe["depth"].append(self.depth[u])

        for v in G.adj(u):
            if not self.marked[v]:
                self.edgeTo[v] = u
                self.depth[v] = self.depth[u] + 1
                self.dfs(G, v)

    def getDepth(self, v):
        return self.depth[v]

    def getNPE(self):
        return self.npe
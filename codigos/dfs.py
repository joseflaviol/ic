class DepthFirstSearch:

    def __init__(self, G, s, terminais):
        self.terminais = terminais
        self.G = G
        self.visited = [False] * G.v 
        self.depth = [None] * G.v 
        self.depth[s] = 0
        self.N = []
        self.D = []
        self.dfs(s)

    def dfs(self, s): 
        
        self.visited[s] = True
        pilha = [s]

        while pilha:
            u = pilha.pop()

            self.N.append(u)
            self.D.append(self.depth[u])

            for v in self.G.adj(u):
                if not self.visited[v]:
                    self.visited[v] = True
                    self.depth[v] = self.depth[u] + 1 
                    pilha.append(v)

    def NPE(self):
        return (self.N, self.D)
from dfs import DepthFirstSearch

class NPE:

    def __init__(self, G):
        dfs = DepthFirstSearch(G, 0)
        self.npe = dfs.getNPE()
    
    def get(self):
        return self.npe

    def decode(self):
        N = len(self.npe["node"])
        n = self.npe["node"]
        d = self.npe["depth"]
        edges = []
        lookup = [0] * N

        for i in range(1, N):
            j = lookup[d[i] - 1]
            edges.append((j, n[i]))
            lookup[d[i]] = n[i]
        
        return edges
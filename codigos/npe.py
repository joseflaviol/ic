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
    
    def SPRN(self, p, a):
        n = self.npe["node"]
        d = self.npe["depth"]

        ia = n.index(a)
        ip = n.index(p)
        il = ip + 1

        while il < len(n) and d[il] > d[ip]:
            il = il + 1
        
        rp = range(ip, il)

        N = []
        D = []

        for i in range(0, ia + 1):
            if i not in rp:
                N.append(n[i])
                D.append(d[i])
        
        for i in rp:
            N.append(n[i])
            D.append(d[i] - d[ip] + d[ia] + 1)

        for i in range(ia + 1, len(n)):
            if i not in rp:
                N.append(n[i])
                D.append(d[i])

        return (N, D)
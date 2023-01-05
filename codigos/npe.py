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
    
    '''
        TO DO:
            -   aleatorizar a escolha do vertice p (checar artigo)
            -   aleatorizar a escolha da aresta (r, a) (checar artigo)
    '''

    def TBRN2(self, p, r, a):
        n = self.npe["node"]
        d = self.npe["depth"]

        ip = n.index(p)
        ir = n.index(r)
        ia = n.index(a)

        ep = ip + 1
        rp = [p] 

        while ep < len(n) and d[ep] > d[ip]:
            rp.append(n[ep])
            ep += 1

        er = ir + 1
        rr = [r] 

        while er < len(n) and d[er] > d[ir]:
            rr.append(n[er])
            er += 1

        Ntmp = []
        Dtmp = []

        for i in range(ir, er):
            Ntmp.append(n[i])
            Dtmp.append( d[i] - d[ir] + d[ia] + 1 )

        N = []
        D = []

        for i in range(0, ia + 1):
            if i < ip or i >= ep:
                N.append(n[i])
                D.append(d[i])

        ix = ir 
        fx = None 

        while ix != ip:

            for i in range(ix - 1, ip - 1, -1):
                if d[i] == d[ix] - 1:
                    fx = i 
                    break 

            ex = fx + 1
            
            while ex < len(n) and d[ex] > d[fx]:
                ex += 1    

            aux_ix = Ntmp.index(n[ix])

            for i in range(fx, ex):
                if n[i] not in rr:
                    rr.append(n[i])
                    Ntmp.append(n[i])
                    Dtmp.append(d[i] - d[fx] + Dtmp[aux_ix] + 1)
            
            ix = fx

        N += Ntmp
        D += Dtmp

        for i in range(ia + 1, len(n)):
            if i < ip or i >= ep:
                N.append(n[i])
                D.append(d[i])

        return (N, D)
    
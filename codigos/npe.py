import random
from dfs import DepthFirstSearch

class NPE:

    def __init__(self, G, terminals):
        self.G = G
        self.terminals = terminals
        self.s = random.randint(0, G.v - 1)
        dfs = DepthFirstSearch(G, self.s, terminals)
        self.n, self.d = dfs.NPE()
    
    def setN(self, n):
        self.n = n 
    
    def setD(self, d):
        self.d = d

    def get(self):
        return (self.n, self.d)

    def decode(self):
        custo = 0
        N = len(self.n)
        n = self.n
        d = self.d
        edges = []
        lookup = [self.s] * N

        for i in range(1, N):
            j = lookup[d[i] - 1]
            edges.append((j, n[i]))
            custo += self.G.adj(j)[n[i]]
            lookup[d[i]] = n[i]
        
        return (custo, edges)
    
    def SPRN(self):
        n = self.n
        d = self.d

        ip = random.randint(1, len(n) - 1)
        
        il = ip + 1

        while il < len(n) and d[il] > d[ip]:
            il = il + 1
        
        rp = range(ip, il)

        ia = None 
        aux = 0

        while ia == None and aux < 10:
            try:
                ia = n.index( random.choice(list( self.G.adj(n[ip]).keys() )))
                if ia in rp:
                    ia = None 
            except ValueError:
                ia = None 
            aux += 1
        
        if ia == None:
            return (n, d)

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

    def TBRN(self):
        n = self.n
        d = self.d

        ip = random.randint(1, len(n) - 1)

        ep = ip + 1
        rp = [n[ip]] 

        while ep < len(n) and d[ep] > d[ip]:
            rp.append(n[ep])
            ep += 1

        rp_aux = range(ip, ep)

        ir = random.randint(ip, ep - 1)

        er = ir + 1
        rr = [n[ir]]

        while er < len(n) and d[er] > d[ir]:
            rr.append(n[er])
            er += 1

        rr_aux = range(ir, er) 

        ia = None 
        aux = 0

        while ia == None and aux < 10:
            try:
                ia = n.index( random.choice(list( self.G.adj(n[ir]).keys() )))
                if ia in rr_aux or ia in rp_aux:
                    ia = None 
            except ValueError:
                ia = None 
            aux += 1
        
        if ia == None:
            return (n, d)

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
    
    def isTerminal(self, v):
        return v in self.terminals

    def isLeaf(self, i):
        for j in range(i + 1, len(self.n)):
            if self.d[j] == self.d[i] + 1:
                return False 
        return True
 
    def father(self, i):
        f = None 
        for j in range(i - 1, -1, -1):
            if self.d[j] == self.d[i] - 1:
                f = j
                break 
        return f

    def redux(self, redux_rate):
        for i in range(len(self.n) - 1, -1, -1):
            if not self.isTerminal(self.n[i]) and self.isLeaf(i): #and not self.isTerminal(n[self.father(i)]):
                r = random.randint(0, 10) / 100
                if r < redux_rate:
                    del self.n[i]
                    del self.d[i]
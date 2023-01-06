from graph import Graph
from dfs import DepthFirstSearch
from npe import NPE

def main():
    
    vertices, arestas = (int(x) for x in input().split())

    g = Graph(vertices)

    for _ in range(arestas):
        discard, u, v, w = input().split()
        g.addEdge(int(u) - 1, int(v) - 1, int(w))
    
    t = int(input())
    terminais = []

    for i in range(t):
        discard, ti = input().split()
        terminais.append(int(ti) - 1) 

    print(terminais)

    npe = NPE(g, terminais)

    custo, arestas = npe.decode()

    print(custo)

    menor = custo
    redux_rate = 0.2

    for _ in range(50):
        npe = NPE(g, terminais)
        for _ in range(30):
            #n, d = npe.SPRN()
            npe.SPRN()
            n, d = npe.TBRN()
            #print(n)
            #print(d)
            npe.setN(n)
            npe.setD(d)
            npe.redux(redux_rate)
            custo, _ = npe.decode()
            if custo < menor:
                menor = custo
            print(custo)
    
    print("Menor: %d" % (menor))

main()
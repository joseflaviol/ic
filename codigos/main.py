from graph import Graph
from dfs import DepthFirstSearch
from npe import NPE

def main():
    g = Graph(oriented = False)

    g.setV(17)

    g.addEdge(0, 1)
    g.addEdge(1, 3)
    g.addEdge(3, 16)
    g.addEdge(0, 2)
    g.addEdge(2, 4)
    g.addEdge(4, 5)
    g.addEdge(5, 6)
    g.addEdge(6, 9)
    g.addEdge(9, 10)
    g.addEdge(5, 7)
    g.addEdge(7, 8)
    g.addEdge(4, 13)
    g.addEdge(4, 14)
    g.addEdge(4, 15)
    g.addEdge(2, 11)
    g.addEdge(0, 12)

    #print(g)

    dfs = DepthFirstSearch(g, 0)

    print("node: " + str(dfs.getNPE()["node"]))
    print("depth: " + str(dfs.getNPE()["depth"]))

    npe = NPE(g)

    print(npe.decode())

    (N, D) = npe.SPRN(6, 3)

    print("node: " + str(N))
    print("depth: " + str(D))

    (N, D) = npe.TBRN2(5, 10, 3)

    print("node: " + str(N))
    print("depth: " + str(D))

main()
from graph import Graph
from dfs import DepthFirstSearch
from npe import NPE

def main():
    g = Graph(oriented = True)

    g.setV(16)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(0, 3)
    g.addEdge(2, 4)
    g.addEdge(2, 8)
    g.addEdge(4, 5)
    g.addEdge(5, 6)
    g.addEdge(5, 7)
    g.addEdge(8, 9)
    g.addEdge(9, 10)
    g.addEdge(10, 11)
    g.addEdge(10, 12)
    g.addEdge(9, 13)
    g.addEdge(8, 14)
    g.addEdge(14, 15)

    #print(g)

    dfs = DepthFirstSearch(g, 0)

    print("node: " + str(dfs.getNPE()["node"]))
    print("depth: " + str(dfs.getNPE()["depth"]))

    npe = NPE(g)

    print(npe.decode())

main()
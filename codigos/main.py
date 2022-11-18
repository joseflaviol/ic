from graph import Graph
from edge_weighted_graph import EdgeWeightedGraph
from steiner_tree import SteinerTree
from dfs import DepthFirstSearch
from npe import NPE

def main():
    g = Graph(oriented = True)

    g.setV(13)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 8)
    g.addEdge(1, 7)
    g.addEdge(2, 3)
    g.addEdge(2, 4)
    g.addEdge(3, 5)
    g.addEdge(3, 10)
    g.addEdge(4, 6)
    g.addEdge(6, 9)
    g.addEdge(6, 12)
    g.addEdge(10, 11)

    #print(g)

    dfs = DepthFirstSearch(g, 0)

    print("node: " + str(dfs.getNPE()["node"]))
    print("depth: " + str(dfs.getNPE()["depth"]))

    npe = NPE(g)

    print(npe.decode())

    (N, D) = npe.SPRN(10, 8)

    print("node: " + str(N))
    print("depth: " + str(D))

def main2():

    g = EdgeWeightedGraph(6, 8)

    g.addEdge(0, 1, 5)
    g.addEdge(0, 2, 3)
    g.addEdge(1, 2, 10)
    g.addEdge(2, 3, 1)
    g.addEdge(3, 4, 50)
    g.addEdge(4, 1, 30)
    g.addEdge(0, 3, 40)
    g.addEdge(4, 5, 100)

main2()
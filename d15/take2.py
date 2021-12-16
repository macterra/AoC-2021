from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import shortest_path

input = """
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""

def makeGraph(input):
    graph = []
    lines = input.split('\n')
    for line in lines:
        graph.append([int(n) for n in line])
    return csr_matrix(graph)

graph = makeGraph(input)
print(graph)

dist_matrix, predecessors = shortest_path(csgraph=graph, directed=False, return_predecessors=True)

print(dist_matrix)
print(predecessors)

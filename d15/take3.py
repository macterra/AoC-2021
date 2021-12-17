import astar


input = """1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581"""


class ShortPath(astar.AStar):
    def __init__(self, input):
        print(input)
        grid = []
        lines = input.split('\n')
        for line in lines:
            grid.append([int(n) for n in line])
        print(grid)            
        self.grid = grid
        self.h = len(grid)
        self.w = len(grid[0])

    def neighbors(self, node):
        x = node%self.w
        y = node//self.w
        print(f"neighbors {node} {x} {y}")

        if x > 0:
            if x+1 < self.w:
            else:
        else:

sp = ShortPath(input)
sp.neighbors(16)

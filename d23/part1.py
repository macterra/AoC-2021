import multi_agent_path_planning.centralized.cbs as cbs

input1 = """#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########"""

input2 = """#############
#...........#
###A#D#B#C###
  #B#C#D#A#
  #########"""

class Agent:
    def __init__(self, c, start):
        self.name = c
        self.start = start 
        self.goal = []

def makeEnv(input):
    lines = input.split('\n')
    for line in lines:
        print(line)

    w = len(lines[0])
    h = len(lines)
    dimensions = [w, h]
    print(dimensions)

    obstacles = []
    agents = []

    for y in range(h):
        for x in range(len(lines[y])):
            c = lines[y][x]
            if c == '#':
                obstacles.append((x,y))
            elif c in "ABCD":
                agents.append(Agent(c, [x, y]))
            print(x, y, lines[y][x])
            
    env = cbs.Environment(dimensions, agents, obstacles)

makeEnv(input1)        

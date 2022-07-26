# use graph
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors

inputFile = open("janitorin.txt", "r")
outputFile = open("janitorout.txt", "w")

line1 = inputFile.readline().split()
row = int(line1[0])
column = int(line1[1])
changes = int(line1[2])

# converting input data to 2d array
floor = []
for _ in range(row):
    line = inputFile.readline().split()
    floor.append(line)

# convert input into graph form (dictionary of each element, with neighbors)
graph = {}
for i in range(row):
    for j in range(column):
        if i == 0 and j == 0:
            graph[f"{i}{j}"] = {"height": int(floor[i][j]), "neighbours": ["01", "10"]}
        elif i == 0 and j == column - 1:
            graph[f"{i}{j}"] = {"height": int(floor[i][j]), "neighbours": [f"0{j-1}", f"1{j}"]}
        elif i == row - 1 and j == 0:
            graph[f"{i}{j}"] = {"height": int(floor[i][j]), "neighbours": [f"{i}1", f"{i-1}0"]}
        elif i == row - 1 and j == column - 1:
            graph[f"{i}{j}"] = {"height": int(floor[i][j]), "neighbours": [f"{i}{j-1}", f"{i-1}{j}"]}
        elif i == 0:
            graph[f"{i}{j}"] = {"height": int(floor[i][j]), "neighbours": [f"{i}{j-1}", f"{i}{j+1}", f"{i+1}{j}"]}
        elif i == row - 1:
            graph[f"{i}{j}"] = {"height": int(floor[i][j]), "neighbours": [f"{i}{j-1}", f"{i}{j+1}", f"{i-1}{j}"]}
        elif j == 0:
            graph[f"{i}{j}"] = {"height": int(floor[i][j]), "neighbours": [f"{i+1}{j}", f"{i-1}{j}", f"{i}{j+1}"]}
        elif j == column - 1:
            graph[f"{i}{j}"] = {"height": int(floor[i][j]), "neighbours": [f"{i+1}{j}", f"{i-1}{j}", f"{i}{j-1}"]}
        else:
            graph[f"{i}{j}"] = {"height": int(floor[i][j]), "neighbours": [f"{i+1}{j}", f"{i-1}{j}", f"{i}{j+1}", f"{i}{j-1}"]}

# weighted dfs definition
marked = []
def dfs(element):
    print('hi')
    marked.append(element)
    for neighbour in graph[element]["neighbours"]:
        if neighbour not in marked and graph[neighbour]["height"] < graph[element]["height"]:
            dfs(neighbour)

def run():
    print(graph)
    print('\n\n')
    counter = 0
    while len(marked) < row * column:
        highest = -1
        cur = ""

        for vertex in graph:
            if vertex not in marked:
                height = graph[vertex]["height"]
                if height > highest:
                    highest = height
                    cur = vertex
        counter += 1
        dfs(cur)

    outputFile.write("%d\n" % (counter))

run()

for _ in range(changes):
    line = inputFile.readline().split()
    i = int(line[0]) - 1
    j = int(line[1]) - 1
    new = int(line[2])
    graph[f"{i}{j}"]['height'] = new
    marked = []
    run()




# call dfs, iterate through neighbors with a lower height and unmarked

# keep calling dfs until all elements are marked
# return number of times dfs was called

# rinse and repeat for each change




# iterate until all tiles are washed
#   'pour' on highest unwashed tile
#   illustrate the pouring process to all adjacent elements, and their adjacent elements, so on and so forth
# return number of times iterated


inputFile.close()
outputFile.close()
import os

class Vertex:
    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y

    def __str__ (self):
        return str(self.label) + " " + str(self.x) + " " + str(self.y)

class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __str__ (self):
        return str(self.start) + " " + str(self.end) + " " + str(self.weight)




def euclideanDistance(v1: Vertex, v2: Vertex):
    return ((v1.x - v2.x)**2 + (v1.y - v2.y)**2)**0.5

def shortestDistance(fileInput: str):
    filePath = os.path.join(os.path.dirname(__file__), fileInput)

    with open(filePath, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        first_line = lines[0].strip().split()
        nVertices, nEdges = int(first_line[0]), int(first_line[1])

        last_line = lines[-1].strip().split()
        start, goal = int(last_line[0]), int(last_line[1])


    lines = lines[1:-1]

    # Extract vertex information
    vertices = []
    for line in lines[2:nVertices + 2]:
        line = line.strip().split()
        k, x, y = int(line[0]), float(line[1]), float(line[2])
        input = Vertex(k, x, y)
        vertices.append(input)

    # Extract edge information
    edges = []
    for line in lines[nVertices + 3:nVertices + nEdges + 3]:
        line = line.strip().split()
        i, j, w = int(line[0]), int(line[1]), float(line[2])
        input = Edge(i, j, w)
        edges.append(input)


    # Find the start and goal vertices
    # Find the start and goal vertices without using next
    start_vertex = None
    goal_vertex = None
    for vertex in vertices:
        if vertex.label == start:
            start_vertex = vertex
        if vertex.label == goal:
            goal_vertex = vertex
        if start_vertex and goal_vertex:
            break

    # Calculate the Euclidean distance
    distance_between_start_goal = 0.0
    print(start_vertex)
    print(start)
    print(goal_vertex)
    print(goal)

    if start_vertex and goal_vertex:
        distance_between_start_goal = euclideanDistance(start_vertex, goal_vertex)
    else:
        print("Start or goal vertex not found.")


    print("The number of vertices and edges in the graph: " + str(nVertices) + " " + str(nEdges))
    print("The start and the goal vertices: " + str(start) + " " + str(goal))
    print("The Euclidean distance between the start and the goal vertices is calculated using their coordinates: " + str(distance_between_start_goal))
    print("The vertices on the shortest path, in order from the start to the goal: ")
    print("The length (weight) of the shortest path: ")
    print("The vertices on the longest path, in order from the start to the goal: ")
    print("The length (weight) of the longest path: ")
    file.close()

if __name__ == '__main__':
    # Test the function
    #fileName = input("Please enter the name of the input file: ")
    fileName = "a3-sample.txt"
    shortestDistance(fileName.strip())
    
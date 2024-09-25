import os
import minHeap

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
    # Get the file path of the input file and open it
    filePath = os.path.join(os.path.dirname(__file__), fileInput)

    # Read the file and extract the information from it
    with open(filePath, 'r', encoding="utf-8") as file:
        lines = file.readlines()
        first_line = lines[0].strip().split()
        nVertices, nEdges = int(first_line[0]), int(first_line[1])

        last_line = lines[-1].strip().split()
        start, goal = int(last_line[0]), int(last_line[1])

    #Remove the first and last line from the list as they are not needed for the rest of the program
    lines = lines[1:-1]



    # Extract vertex information
    vertices = []
    for line in lines[1:nVertices + 1]:
        line = line.strip().split()
        label, x, y = int(line[0]), float(line[1]), float(line[2])
        input = Vertex(label, x, y)
        vertices.append(input)

    # Extract edge information
    edges = []
    for line in lines[nVertices + 1:nVertices + nEdges + 1]:
        line = line.strip().split()
        i, j, w = int(line[0]), int(line[1]), float(line[2])
        input = Edge(i, j, w)
        edges.append(input)

    for vertex in vertices:
        if vertex.label == start:
            start = vertex
        elif vertex.label == goal:
            goal = vertex

    if int == type(start) or type(goal) == int:
        return "The start and goal vertices are not in the graph"
    

    # Find the start and goal vertices
    start_vertex = None
    goal_vertex = None
    for vertex in vertices:
        if vertex.label == start:
            start_vertex = vertex
        if vertex.label == goal:
            goal_vertex = vertex
        if start_vertex and goal_vertex:
            break

    MinHeap = minHeap.MinHeap()

    
    answer = minHeap.dijkstra(vertices, edges, start, goal)

    # Find the shortest path
    shortest_path = []
    shortest_path_length = 0

    
    # Find the longest path
    longest_path = []
    longest_path_length = 0


    

    # Print the information extracted from the file to the console
    print("The number of vertices and edges in the graph: " + str(nVertices) + " " + str(nEdges))
    print("The start and the goal vertices: " + str(start) + " " + str(goal))
    print("The Euclidean distance between the start and the goal vertices is calculated using their coordinates: " + str(euclideanDistance(start_vertex, goal_vertex)))

    print("The vertices on the shortest path, in order from the start to the goal: ")
    print("The length (weight) of the shortest path: ")
    print("The vertices on the longest path, in order from the start to the goal: ")
    print("The length (weight) of the longest path: ")

    # Close the file
    file.close()

if __name__ == '__main__':
    # Test the function
    #fileName = input("Please enter the name of the input file: ")
    fileName = "a3-sample.txt"
    shortestDistance(fileName.strip())
    
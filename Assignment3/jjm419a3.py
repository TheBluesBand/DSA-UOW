#!/usr/bin/env python3

import os

#------------------------------------------------------------

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return 2 * i + 1

    def rightChild(self, i):
        return 2 * i + 2

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def heapifyUp(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def heapifyDown(self, i):
        largest = i
        left = self.leftChild(i)
        right = self.rightChild(i)

        if left < len(self.heap) and self.heap[left] < self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] < self.heap[largest]:
            largest = right

        if largest != i:
            self.swap(i, largest)
            self.heapifyDown(largest)

    def push(self, item):
        self.heap.append(item)
        self.heapifyUp(len(self.heap) - 1)

    def pop(self):
        if len(self.heap) == 0:
            return None

        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.heapifyDown(0)
        return root

    def empty(self):
        return len(self.heap) == 0
    
#------------------------------------------------------------

def dijkstraAlgorithm(vertices, edges, startVertex, endVertex):
    # Initialize distances and previous nodes
    for vertex in vertices:
        vertex.distance = float('inf')
        vertex.previous = None
    startVertex.distance = 0

    # Create a priority queue using the custom MinHeap class
    unvisitedPoints = MinHeap()
    for vertex in vertices:
        unvisitedPoints.push(vertex)

    # Main loop
    while not unvisitedPoints.empty():
        current_vertex = unvisitedPoints.pop()

        # Check if the current vertex is the end vertex
        if current_vertex == endVertex:
            # Reconstruct the shortest path
            path = []
            while current_vertex:
                path.insert(0, current_vertex)
                current_vertex = current_vertex.previous
            return endVertex.distance, path

        # Explore neighbors
        for edge in edges:
            if edge.start == current_vertex.label:
                neighbor = next(vertex for vertex in vertices if vertex.label == edge.end)
                tentative_distance = current_vertex.distance + edge.weight
                if tentative_distance < neighbor.distance:
                    neighbor.distance = tentative_distance
                    neighbor.previous = current_vertex
                    # Update the priority queue
                    unvisitedPoints.push(neighbor)

    # If the end vertex was not found, no path exists
    return None, []

#------------------------------------------------------------

def dfs_longest_path(vertices, edges, current_vertex, goal_vertex, visited, current_weight, max_weight, path, current_path, path_index, max_path_index):
    visited[current_vertex.label] = True
    current_path[path_index] = current_vertex
    path_index += 1

    if current_vertex == goal_vertex:
        if current_weight > max_weight[0]:
            max_weight[0] = current_weight
            max_path_index[0] = path_index
            for i in range(path_index):
                path[i] = current_path[i]
    else:
        for edge in edges:
            if edge.start == current_vertex.label:
                neighbor = next(v for v in vertices if v.label == edge.end)
                if not visited[neighbor.label]:
                    dfs_longest_path(vertices, edges, neighbor, goal_vertex, visited, current_weight + edge.weight, max_weight, path, current_path, path_index, max_path_index)

    visited[current_vertex.label] = False

def find_longest_path(vertices, edges, start, goal):
    """
    Finds the longest simple path from vertex 'start' to vertex 'goal' using DFS with backtracking.
    It prints the longest path and its length.
    Args:
        vertices: A list of Vertex objects.
        edges: A list of Edge objects.
        start: The starting Vertex object.
        goal: The goal Vertex object.
    """
    V = len(vertices)
    visited = {v.label: False for v in vertices}
    path = [None] * V
    current_path = [None] * V
    max_weight = [-1]
    max_path_index = [0]
    path_index = 0

    dfs_longest_path(vertices, edges, start, goal, visited, 0, max_weight, path, current_path, path_index, max_path_index)


    if max_weight[0] == -1:
        print(f"No path found from vertex {start.label} to vertex {goal.label}")
        return None, []
    else:
        longest_path = [path[i] for i in range(max_path_index[0])]
        return max_weight[0], longest_path

#------------------------------------------------------------

class Vertex:
    def __init__(self, label, x, y):
        self.label = label
        self.x = x
        self.y = y
        self.distance = float('inf')

    def __lt__(self, other):
        return self.distance < other.distance

    def __str__ (self):
        return str(self.label)
    
    def __repr__(self):
        return self.__str__()

class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight

    def __str__ (self):
        return str(self.start) + " " + str(self.end) + " " + str(self.weight)
    
    def __repr__(self):
        return self.__str__()
    
def euclideanDistance(vertex1: Vertex, vertex2: Vertex):
  """Calculates the Euclidean distance between two Vertex objects.

  Args:
    vertex1: The first Vertex object.
    vertex2: The second Vertex object.

  Returns:
    The Euclidean distance between the two vertices.
  """

  dx = vertex1.x - vertex2.x
  dy = vertex1.y - vertex2.y
  distance = ((dx ** 2) + (dy ** 2)) ** 0.5
  return round(distance, 4)
    

#------------------------------------------------------------

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

    # Find the start and goal vertices
    for vertex in vertices:
        if vertex.label == start:
            start = vertex
        elif vertex.label == goal:
            goal = vertex

    # Extract edge information
    edges = []
    for line in lines[nVertices + 1:nVertices + nEdges + 1]:
        line = line.strip().split()
        i, j, w = int(line[0]), int(line[1]), float(line[2])
        input = Edge(i, j, w)
        edges.append(input)

    if int == type(start) or type(goal) == int:
        return "The start and goal vertices are not in the graph"


    # Print the information extracted from the file to the console
    print("===============================================================================================================================")
    print("The number of vertexes in the graph: " + str(nVertices))
    print("The number of edges in the graph: " + str(nEdges))
    print("The start vertexes: " + str(start))
    print("The end vertexes: " + str(goal))
    print("===============================================================================================================================")
    print("The Euclidean distance between the start and the goal vertexes: " + str(euclideanDistance(start, goal)))

    shortestWeight, shortestPath = dijkstraAlgorithm(vertices, edges, start, goal)
    print("Shortest path: ", end="")
    for i in range(len(shortestPath)):
        if i != len(shortestPath) - 1:
            print(shortestPath[i].label, end=" -> ")
        else:
            print(shortestPath[i].label)
    print("The length (weight) of the shortest path: " + str(int(shortestWeight)))


    LongestWeight, LongestPath = find_longest_path(vertices, edges, start, goal)
    print("Longest path: ", end="")
    for i in range(len(LongestPath)):
        if i != len(LongestPath) - 1:
            print(LongestPath[i].label, end=" -> ")
        else:
            print(LongestPath[i].label)
    print("The length of the longest path: " + str(int(LongestWeight)))

    print("===============================================================================================================================")
    

    # Close the file
    file.close()

if __name__ == '__main__':
    # Test the function
    #fileName = input("Please enter the name of the input file: ")
    fileName = "a3-sample.txt"
    shortestDistance(fileName.strip())
    
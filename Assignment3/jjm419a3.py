#!/usr/bin/env python3

import os

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

class Vertex:
    def __init__(self, label, x, y):
        """
        Initializes a Vertex object.
        Args:
            label: The label of the vertex (usually an integer or string).
            x: The x-coordinate of the vertex.
            y: The y-coordinate of the vertex.
        """
        self.label = label
        self.x = x
        self.y = y
        self.distance = float('inf')  # Distance from the source vertex, used in shortest path algorithms

    def __lt__(self, other):
        """
        Less-than comparison based on distance.
        Args:
            other: Another Vertex object to compare with.
        Returns:
            True if this vertex's distance is less than the other vertex's distance.
        """
        return self.distance < other.distance

    def __str__(self):
        """
        String representation of the vertex.
        Returns:
            The label of the vertex as a string.
        """
        return str(self.label)
    
    def __repr__(self):
        """
        Official string representation of the vertex.
        Returns:
            The label of the vertex as a string.
        """
        return self.__str__()

class Edge:
    def __init__(self, start, end, weight):
        """
        Initializes an Edge object.
        Args:
            start: The label of the start vertex.
            end: The label of the end vertex.
            weight: The weight of the edge.
        """
        self.start = start
        self.end = end
        self.weight = weight

    def __str__(self):
        """
        String representation of the edge.
        Returns:
            A string in the format "start end weight".
        """
        return str(self.start) + " " + str(self.end) + " " + str(self.weight)
    
    def __repr__(self):
        """
        Official string representation of the edge.
        Returns:
            A string in the format "start end weight".
        """
        return self.__str__()
    
def euclidean_distance(vertex1: Vertex, vertex2: Vertex):
  """
  Calculates the Euclidean distance between two Vertex objects.
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
    


def dijkstra_algorithm(vertices, edges, startVertex, endVertex):
    """
    Finds the shortest path from 'startVertex' to 'endVertex' using Dijkstra's algorithm.
    Args:
        vertices: A list of Vertex objects.
        edges: A list of Edge objects.
        startVertex: The starting Vertex object.
        endVertex: The goal Vertex object.
    Returns:
        A tuple containing the shortest distance and the path itself as a list of Vertex objects.
        If no path exists, returns (None, []).
    """

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
    """
    Performs a depth-first search to find the longest path from 'current_vertex' to 'goal_vertex'.
    Args:
        vertices: A list of Vertex objects.
        edges: A list of Edge objects.
        current_vertex: The current Vertex object in the DFS traversal.
        goal_vertex: The goal Vertex object to reach.
        visited: A dictionary to keep track of visited vertices.
        current_weight: The current weight of the path being explored.
        max_weight: A list containing the maximum weight found so far.
        path: A list to store the longest path found.
        current_path: A list to store the current path being explored.
        path_index: The current index in the current_path list.
        max_path_index: A list containing the index of the longest path found.
    """

    # Mark the current vertex as visited
    visited[current_vertex.label] = True
    
    # Add the current vertex to the current path
    current_path[path_index] = current_vertex
    path_index += 1

    # Check if the current vertex is the goal vertex
    if current_vertex == goal_vertex:
        # If the current path weight is greater than the maximum weight found so far
        if current_weight > max_weight[0]:
            # Update the maximum weight
            max_weight[0] = current_weight
            # Update the maximum path index
            max_path_index[0] = path_index
            # Copy the current path to the path array
            for i in range(path_index):
                path[i] = current_path[i]
    else:
        # Iterate over all edges to find neighbors of the current vertex
        for edge in edges:
            if edge.start == current_vertex.label:
                # Find the neighbor vertex
                neighbor = next(v for v in vertices if v.label == edge.end)
                # If the neighbor has not been visited
                if not visited[neighbor.label]:
                    # Recursively call dfs_longest_path for the neighbor
                    dfs_longest_path(vertices, edges, neighbor, goal_vertex, visited, current_weight + edge.weight, max_weight, path, current_path, path_index, max_path_index)

    # Mark the current vertex as unvisited (backtrack)
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

def findDistance(fileInput: str):
    """
    Processes the input file to extract vertices and edges, and finds the shortest and longest paths between the start and goal vertices.
    Args:
        fileName: The name of the input file containing the graph data.
    Returns:
        A string message if the start or goal vertices are not in the graph.
        Otherwise, prints statistics about the graph and the shortest and longest paths.
    """

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
    print("The Euclidean distance between the start and the goal vertexes: " + str(euclidean_distance(start, goal)))

    shortestWeight, shortestPath = dijkstra_algorithm(vertices, edges, start, goal)
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
    fileName = input("Please enter the name of the input file: ")
    #fileName = "a3-sample.txt"
    findDistance(fileName.strip())
    
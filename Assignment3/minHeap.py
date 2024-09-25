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

def dijkstra(vertices, edges, startVertex, endVertex):
    """
    Finds the shortest path from a given start vertex to a specific end vertex using Dijkstra's algorithm.

    Args:
        vertices: A list of Vertex objects.
        edges: A list of Edge objects.
        startVertex: The starting Vertex object.
        endVertex: The ending Vertex object.

    Returns:
        The shortest distance between the start vertex and the end vertex, or None if no path exists.
    """

    # Initialize distances and previous nodes
    distances = {vertex: float('inf') for vertex in vertices}
    distances[startVertex] = 0
    previous = {vertex: None for vertex in vertices}

    # Create a priority queue using the custom MinHeap class
    unvisitedPoints = MinHeap()
    for vertex in vertices:
        unvisitedPoints.push((distances[vertex], vertex))

    # Main loop
    while not unvisitedPoints.empty():
        _, current_vertex = unvisitedPoints.pop()

        # Check if the current vertex is the end vertex
        if current_vertex == endVertex:
            return distances[endVertex]

        # Explore neighbors
        for neighbor, edge in [(v, e) for (u, v, e) in edges if u == current_vertex]:
            tentative_distance = distances[current_vertex] + edge.weight
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                previous[neighbor] = current_vertex
                # Update the priority queue
                unvisitedPoints.push((tentative_distance, neighbor))

    # If the end vertex was not found, no path exists
    return None
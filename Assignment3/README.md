## Assessment 3 - CSCI203

### Jake McCoy - 7161955

### Purpose

This project contains a Python script that finds the shortest and longest paths between two vertices in a weighted graph. The graph is represented by vertices and edges, and the input is provided through a text file.

- **Number of Vertexes in the graph:** Shows the number of Vertexes in the graph.
- **Number of Edges in the graph:** Shows the number of Edges in the graph
- **The Start Vertex:** The starting vertex
- **The End Vertex:** The ending vertex
- **Euchlidean Distance from Start to End Vertex:** The euchlidean distance from the Start to the End Vertex
- **The shortest path from Start to End Vertex:** The shortest path from the Start to the End Vertex via the Edges
- **The weight of the shortest path:** The weight of the shortest path from the Start to the End Vertex via the Edges weight
- **The longest path from Start to End Vertex:** The longest path from the Start to the End Vertex via the Edges
- **The weight of the longest path:** The weight of the longest path from the Start to the End Vertex via the Edges weight

### How It Works

1. **Import Necessary Modules:** Imports the `os` module. The file called `jjm419a3.py` contains all of the neccessary classes (`Vertex`, `Edge`, `MinHeap`) and the functions (`find_longest_path`, `dfs_longest_path`, `dijkstra_algorithm` and `euclidean_distance`).

   - `os` was used to find the location of the inputed file after the user has inputted it.
   - `Vertex` Represents a Vertex in the graph.
   - `Edge` Represents a Edge in the graph.
   - `MinHeap` The heap we use in Dijkstras Algorithm to find the shortest length
   - `find_longest_path` Finds the longest simple path from vertex 'start' to vertex 'goal' using DFS with backtracking.
   - `dfs_longest_path` Performs a depth-first search to find the longest path from 'current_vertex' to 'goal_vertex'.
   - `dijkstra_algorithm` Finds the shortest path from 'startVertex' to 'endVertex' using Dijkstra's algorithm.
   - `euclidean_distance` Calculates the Euclidean distance between two Vertex objects.

2. **Main Initialization**: The main function runs and gets the user's input for the start and goal vertices. It then reads the graph data from the specified input file (a3-sample.txt).
3. **Open File**: Opens the specified file in read mode with UTF-8 encoding. If the file name/path is invalid, the script stops.
4. **Process File Content**:

   - Reads the number of vertices and edges from the file.
   - Iterates through each line in the file to read the edges.
   - For each edge, it extracts the start vertex, end vertex, and weight, and adds the edge to the graph.

5. **Initialize Graph**: Creates and sets up the graph using the vertices and edges read from the file.

6. **Run Algorithms**:

   - **Dijkstra's Algorithm**: Finds the shortest path from the start vertex to the goal vertex using Dijkstra's algorithm.
   - **DFS Longest Path**: Finds the longest simple path from the start vertex to the goal vertex using Depth-First Search (DFS) with backtracking.

7. **Print Results**:
   - Prints the number of vertices and edges in the graph.
   - Prints the start and goal vertices.
   - Prints the Euclidean distance between the start and goal vertices.
   - Prints the shortest path and its length.
   - Prints the longest path and its length.

### Dependencies

- **os:** The only dependency required is you have the os library installed for python3 (Which should come preinstalled but if not run `pip3 install os`)
- **Python3 Version:** Make sure you are running the latest version of `Python3`. This code was tested on version `Python3 3.12.5`

### Complexity in Big O-Notation

### Data Structures Used: Priority Queue implemented with a List

My solution makes use of two different algorithms one for finding the shortest path and the other for finding the longest path.

#### Depth First Search Algorithm

The complexity of DFS is `O(V+E)` that DFS traverses every Vertex and every Edge at most one time. This means the worst case is the addition of the length of the two inputs (Vertex and Edge).

#### Dijkstra Algorithm

The complexity of this algorithm `0((V+E)⋅logV)`. - `V+E`: Total number of iterations we go through for the algorithm - `logV`: This is the time complexity associated with minHeap operations such as Insert, Delete and Key Update. - `0((V+E)⋅logV)`: The total number of iterations multiplied by the associated complexity of the underlying data structure and its operations.

#### Total Complexity

To find the complexity of the solution we combine the complexities of the worst-case scenarios of the Dijkstras Algorithm and Depth Search First which gives us `0((V+E)⋅logV)+0(V+E)`.

### How to Run

1.  Ensure that the input file is in the same directory as `jjm419a3.py`. For Assignment 3 of CSCI203 the input file is called `a3-sample.txt`
2.  Run the script.

    **Option A**

    - I am using the Python extension in VSCode to run this script. This allows for a button in the top right which will run the file open in the editor.
    - The extension information is below if you want to follow how I did it:
    <table style="padding: 20px">
        <tr>
            <td>
               Python <br />
                Id: ms-python.python <br />
                Description: Python language support with extension access points for IntelliSense (Pylance), Debugging (Python Debugger), linting, formatting, refactoring, unit tests, and more. <br />
                Version: 2024.12.3 <br />
                Publisher: Microsoft <br />
                VS Marketplace Link: https://marketplace.visualstudio.com/items?itemName=ms-python.python <br />
            </td>
        </tr>
    </table>

    **Option B**

    - Open a terminal in the same directory as the `jjm419a2.py` and `a2-sample.txt` are in.
    - Type in the command `./jjm419a3.py`

3.  Enter the file input you want to feed into the script

    - WARNING: Only tested with files with .txt extensions. Also, make sure your .txt follows the format bellow
      - The 1st line contains two integers denoted as nVertices and nEdges, which are the number of vertices and edges in the graph.
      - The 2nd until (nVertices+1)th lines are nVertices triples of the form k x y (an int followed by two doubles):
        - k is the vertex label
        - x is the x‐coordinates of the vertex
        - y is the y‐coordinates of the vertex.
      - Line nVertices+2 until line 121 are nEdges triples of the form i j w (Two ints followed by a double):
        - i is the labels of the start vertex of the edge,
        - j is the labels of the end vertex of the edge,
        - w is the weight of the edge.
          Note: the weight associated with an edge will be greater than or equal to the Euclidean distance between its start and end vertices as determined by their coordinates.
      - The last line in the data file is two vertex labels indicating the start and the goal vertices for which the paths are required. (Two ints)

4.  The script will process the file and display the graph statistics in the terminal.

### Example

**Example Input File**

<table style="padding: 10px">
<tr>
<td>
5 <br />
6 <br />
0 1 2.5 <br />
0 2 1.2 <br />
1 2 1.8 <br />
1 3 2.0 <br />
2 3 2.5 <br />
3 4 1.0 <br />
0 4 <br />
</td>
</tr>
</table>

**Output from Example File**

```terminal
======================================================================
The number of vertexes in the graph: 5
The number of edges in the graph: 6
The start vertexes: 0
The end vertexes: 4
======================================================================
The Euclidean distance between the start and the goal vertexes: 5.0
Shortest path: 0 -> 2 -> 3 -> 4
The length (weight) of the shortest path: 4
Longest path: 0 -> 1 -> 2 -> 3 -> 4
The length of the longest path: 7
======================================================================
```

[comment]: <> (This README was created to provide the reasoning of this code and also how to run it. This will also be here to show people in the future my coding abilities if they are curious how I would solve a given problem)

---
Author: Vighnesh Nayak
Date: 02/11/2023
Modified: 02/11/2023
Topic: Graphs
tags: [ dsa ]
---
# Dijkstra Algorithm.
---

Creating a path tree using Dijkstra's algorithm is a common approach for finding the shortest paths from a single source node to all other nodes in a graph. The resulting path tree is often referred to as a "shortest path tree." Here's a step-by-step algorithm for creating a path tree using Dijkstra's algorithm:

**Input:**
- A weighted, connected graph (represented as an adjacency list or matrix).
- A source node from which you want to find the shortest paths.

**Output:**
- A shortest path tree representing the shortest paths from the source node to all other nodes in the graph.

**Algorithm:**

1. Initialize data structures:
   - Create an empty set of visited nodes.
   - Initialize a list to store the distances from the source node to all other nodes. Initially, set the distance to the source node as 0 and all others as infinity.
   - Create an empty path tree data structure (e.g., a dictionary or array) to store the tree's structure, initially empty.
   - Create a priority queue (min-heap) to store nodes and their associated distances.

2. Add the source node to the priority queue with a distance of 0.

3. While the priority queue is not empty:
   a. Extract the node with the smallest distance from the priority queue. This node becomes the current node.

   b. If the current node is already visited, skip it (as you've already found the shortest path to it).

   c. Mark the current node as visited.

   d. For each unvisited neighboring node of the current node:
      - Calculate the tentative distance from the source node to this neighboring node through the current node.
      - If the tentative distance is less than the recorded distance for the neighboring node:
        - Update the recorded distance for the neighboring node.
        - Add the neighboring node to the priority queue with the new distance.

   e. Update the path tree: For each node visited in step 3c, store the current node as its parent in the path tree.

4. Once the algorithm terminates, the path tree contains the shortest paths from the source node to all other nodes. You can traverse the path tree to find the shortest paths to any specific destination node.

The path tree represents the structure of the shortest paths in the graph, with each node having a parent node on the path back to the source node. It provides not only the shortest distances but also the actual path to reach each node from the source node.

Keep in mind that Dijkstra's algorithm is designed for graphs with non-negative edge weights. If there are negative edge weights in the graph, consider using an algorithm like the Bellman-Ford algorithm, which can handle such cases.
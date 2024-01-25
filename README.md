![BuildStatus](https://github.com/ashvinravi/HW2-BFS/actions/workflows/test.yml/badge.svg?event=push)

# HW2: Breadth-First Search (BFS) 

This project creates a graph class as well as a bfs() method that traverses through each node of the graph using Breadth-First Search (BFS). 

## Description: 
Here are the parameters for passing into the bfs() function: 
   1. self - no need to specify this, but bfs() belongs to the Graph class. How you would call this method is graph.bfs(), where graph is Graph(). 
   2. Source Node - BFS traversal node starts from this node and works down the tree. If node has no edges, BFS only returns the first node IF it exists in the graph. 
   3. (Optional) End node - If end node is specified, bfs() returns the shortest path between both the source node and end node. If end node is not found or path between start and end node does not exist, bfs() returns None. 

## Unit Tests     
The following tests are ran for the Unit Tests: 
   1. Testing a completely empty graph - returns Networkx Exception (neighbors of node that doesn't exist in graph are not found). 
   2. Testing a disconnected empty graph - returns None for path between disconnected nodes. 
   3. Testing a decoy graph - user-created example using just letters as nodes rather than UCSF faculty/papers to grasp BFS better/work with a smaller dataset.
   4. Testing tiny network graph - testing subsetted graph from the full UCSF citation network adjacency list. This tests both traversal, edge cases, as well as shortest path for multiple cases. 
   5. Testing the full citation graph - testing full graph here from the UCSF citation network adjacency list. 

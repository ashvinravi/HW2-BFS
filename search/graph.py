#import queue_obj
from search import queue_obj
import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G
        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """
        Q = queue_obj.Queue()
        G = self.graph
        visited = []
        Q.push([start])
        visited.append(start)
        while (Q.isEmpty() == False):
            path = Q.pop()
            v = path[-1]
            N = G.neighbors(v)
            for w in N:
                if w not in visited:
                    new_path = list(path)
                    new_path.append(w)
                    visited.append(w)
                    if w == end:
                        return new_path
                    Q.push(new_path)
        if end and end not in visited:
            return None
        return visited
""""   
decoy_graph = Graph("data/decoy.adjlist")
a = list(nx.bfs_tree(decoy_graph.graph, 'A'))
print(a)

         
decoy_graph = Graph("data/decoy.adjlist")
source_node = list(decoy_graph.graph.nodes())[0]
traversed_nodes = decoy_graph.bfs(source_node, "M")
print(traversed_nodes)
"""



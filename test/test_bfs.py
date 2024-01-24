# write tests for bfs
import pytest
import random
import networkx as nx
from search import graph
import unittest

def test_empty_graph():
    """
    Tests that function returns exception/error for an empty graph.
    """
    empty_graph = graph.Graph("data/empty.adjlist")

    with pytest.raises(nx.exception.NetworkXError):
        x = empty_graph.bfs('A')
    

def test_disconnected_graph():
    """
    Tests that functon returns error for shortest path between disconnected nodes.
    Disconnected graph.
    """
    disconnected_graph = graph.Graph("data/disconnected.adjlist")

    assert ( disconnected_graph.bfs('A') == ['A', 'D'])
    assert ( disconnected_graph.bfs('B') == ['B', 'C'])

    assert ( disconnected_graph.bfs('A', 'C') == None)
    
def test_bfs_traversal_decoy_graph():
    """
    This unit test verifies whether the BFS traversal/shortest 
    path works on a small graph, using letters. I wrote these 
    tests just to get a better idea of how the BFS algorithm
    should traverse through the graph. The test graph is located 
    in the test.adjlist file. 
    """

    # Does the function implement BFS in the correct order by level? 
    decoy_graph = graph.Graph("data/decoy.adjlist")
    source_node = list(decoy_graph.graph.nodes())[0]
    # Source node is A in this case (first node in adjacency list)
    traversed_nodes = decoy_graph.bfs(source_node)
    assert ( traversed_nodes == ['A', 
                                 'B', 'C', 
                                 'G', 'F', 'D', 
                                 'H', 'J', 'E', 
                                 'I', 'K', 'L', 
                                 'M'] ) 
    # Can BFS traverse graph from different start node? 
    # In this case many nodes will be omitted. 

    traversed_nodes_from_f = decoy_graph.bfs('F')
    assert ( traversed_nodes_from_f == ['F',
                                        'G', 'J',
                                        'H', 'K', 'L',
                                        'I', 'D', 'M',
                                        'E'])

    # Does shortest path algorithm work? Should NOT return all traversed nodes. 
    shortest_path_to_m = decoy_graph.bfs(source_node, "M")
    assert ( shortest_path_to_m == ['A', 'C', 'F', 'J', 'L', 'M'])

    """ Does BFS return the CORRECT shortest path? For this unit test, there are 
    two shortest paths from A to K.
        1. [A, C, D, E, K]
        2. [A, C, F, J, K]
    Because BFS prioritizes by level/which neighbor appears first, it should return the second one.
    """
    shortest_path_to_k = decoy_graph.bfs(source_node, "K")
    assert ( shortest_path_to_k == ['A', 'C', 'F', 'J', 'K'])

    # Shortest path should NOT return traversed nodes and instead should return None.
    shortest_path_to_a = decoy_graph.bfs("M", "A")
    assert ( shortest_path_to_a == None ) 

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    tiny_network_graph = graph.Graph("data/tiny_network.adjlist")
    list_of_nodes = list(tiny_network_graph.graph.nodes())  
    random_node = random.choice(list_of_nodes)

    # Check that tiny network is connected and every node is able to be traversed through. 
    assert ( len(tiny_network_graph.bfs(random_node)) == len(list_of_nodes)), "Not all nodes within the UCSF BMI Faculty are connected."
    
    # Check example case for shortest path. 
    assert ( tiny_network_graph.bfs("Hani Goodarzi", "Martin Kampmann") == ['Hani Goodarzi', '33232663', 'Martin Kampmann'])
    
    # Check that BFS traverses correctly for entire graph 
    assert ( tiny_network_graph.bfs("Hani Goodarzi") == list(nx.bfs_tree(tiny_network_graph.graph, 'Hani Goodarzi')))


def test_bfs(): 
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """

    citation_network_graph = graph.Graph("data/citation_network.adjlist")

    # check BFS traversal from node not in tiny network 
    assert ( citation_network_graph.bfs("Tony Capra") == list(nx.bfs_tree(citation_network_graph.graph, 'Tony Capra')))

    # check that disconnected nodes return None 
    assert ( citation_network_graph.bfs("Jingjing Li", "Tony Capra") == None)

    # check that directionality matters since this is a directed graph! 
    assert ( citation_network_graph.bfs("Tony Capra", "Jingjing Li") != None)

    # Finally, check shortest path algorithm works and is synonymous with nx BFS shortest path. 
    assert ( citation_network_graph.bfs("Tony Capra", "Jimmie Ye") == ['Tony Capra', '32839541', 'Nadav Ahituv', '31784727', 'Neil Risch', '29022597', 'Jimmie Ye'])
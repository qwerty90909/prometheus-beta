from typing import List, Dict, Set

def kosaraju_strongly_connected_components(graph: Dict[int, List[int]]) -> List[List[int]]:
    """
    Find strongly connected components in a directed graph using Kosaraju's Algorithm.
    
    Args:
        graph (Dict[int, List[int]]): Adjacency list representation of the graph
    
    Returns:
        List[List[int]]: List of strongly connected components
    
    Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges
    Space Complexity: O(V)
    """
    def dfs_first_pass(node: int) -> None:
        """First DFS pass to generate the order stack."""
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                dfs_first_pass(neighbor)
        order_stack.append(node)
    
    def dfs_second_pass(node: int, component: List[int]) -> None:
        """Second DFS pass to find strongly connected components."""
        reversed_visited.add(node)
        component.append(node)
        for neighbor in reversed_graph.get(node, []):
            if neighbor not in reversed_visited:
                dfs_second_pass(neighbor, component)
    
    # Handle empty graph
    if not graph:
        return []
    
    # First pass: create order stack
    visited: Set[int] = set()
    order_stack: List[int] = []
    for node in graph:
        if node not in visited:
            dfs_first_pass(node)
    
    # Create reversed graph
    reversed_graph: Dict[int, List[int]] = {}
    for node, neighbors in graph.items():
        for neighbor in neighbors:
            reversed_graph.setdefault(neighbor, []).append(node)
    
    # Second pass: find strongly connected components
    reversed_visited: Set[int] = set()
    strongly_connected_components: List[List[int]] = []
    
    # Process nodes in reverse order of first pass
    while order_stack:
        node = order_stack.pop()
        if node not in reversed_visited:
            component: List[int] = []
            dfs_second_pass(node, component)
            strongly_connected_components.append(component)
    
    return strongly_connected_components
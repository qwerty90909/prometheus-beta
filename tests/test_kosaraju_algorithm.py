import pytest
from src.kosaraju_algorithm import kosaraju_strongly_connected_components

def test_simple_connected_graph():
    """Test a simple graph with two strongly connected components."""
    graph = {
        1: [2],
        2: [3],
        3: [1],
        4: [5],
        5: [6],
        6: [4]
    }
    components = kosaraju_strongly_connected_components(graph)
    
    # Check number of components
    assert len(components) == 2
    
    # Check components content 
    assert sorted(components[0]) == [1, 2, 3] or sorted(components[0]) == [4, 5, 6]
    assert sorted(components[1]) == [1, 2, 3] or sorted(components[1]) == [4, 5, 6]

def test_disconnected_graph():
    """Test a disconnected graph with multiple components."""
    graph = {
        1: [2],
        2: [1],
        3: [4],
        4: [],
        5: [6],
        6: [5]
    }
    components = kosaraju_strongly_connected_components(graph)
    
    # Check number of components
    assert len(components) == 3
    
    # Verify component sizes and structure
    component_sets = [set(component) for component in components]
    assert {1, 2} in component_sets
    assert {3} in component_sets
    assert {5, 6} in component_sets

def test_empty_graph():
    """Test handling of an empty graph."""
    graph = {}
    components = kosaraju_strongly_connected_components(graph)
    assert components == []

def test_single_node_graph():
    """Test a graph with a single node."""
    graph = {1: []}
    components = kosaraju_strongly_connected_components(graph)
    assert len(components) == 1
    assert components[0] == [1]

def test_cyclic_graph():
    """Test a fully connected graph."""
    graph = {
        1: [2],
        2: [3],
        3: [1, 4],
        4: [5],
        5: [3]
    }
    components = kosaraju_strongly_connected_components(graph)
    
    # Verify cyclic structure
    assert len(components) == 2
    component_sets = [set(component) for component in components]
    assert {1, 2, 3, 5} in component_sets
    assert {4} in component_sets
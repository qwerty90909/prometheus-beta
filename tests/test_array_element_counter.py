import pytest
from src.array_element_counter import count_element_occurrences

def test_count_element_occurrences():
    # Test basic functionality
    assert count_element_occurrences([1, 2, 3, 2, 2], 2) == 3
    assert count_element_occurrences(['a', 'b', 'c', 'a'], 'a') == 2
    
    # Test with no occurrences
    assert count_element_occurrences([1, 2, 3], 4) == 0
    
    # Test with empty array
    assert count_element_occurrences([], 5) == 0
    
    # Test with None input
    assert count_element_occurrences(None, 5) == 0
    
    # Test with mixed types
    assert count_element_occurrences([1, '1', 1, '1'], 1) == 2
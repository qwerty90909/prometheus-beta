import pytest
from src.array_counter import count_element_occurrences

def test_count_element_occurrences():
    # Test normal case with multiple occurrences
    assert count_element_occurrences([1, 2, 3, 2, 2, 4], 2) == 3
    
    # Test case with no occurrences
    assert count_element_occurrences([1, 3, 5, 7], 9) == 0
    
    # Test with empty array
    assert count_element_occurrences([], 5) == 0
    
    # Test with None input
    assert count_element_occurrences(None, 5) == 0
    
    # Test with different data types
    assert count_element_occurrences(['a', 'b', 'a', 'c'], 'a') == 2
    
    # Test with mixed types in array
    assert count_element_occurrences([1, '1', 1, '1'], 1) == 2
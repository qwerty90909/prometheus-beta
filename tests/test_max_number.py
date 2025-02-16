import pytest
from src.max_number import find_max_number

def test_find_max_number_positive():
    """Test finding max in a list of positive numbers"""
    assert find_max_number([1, 2, 3, 4, 5]) == 5
    assert find_max_number([10, 5, 8, 12, 3]) == 12

def test_find_max_number_mixed():
    """Test finding max in a list with negative and positive numbers"""
    assert find_max_number([-1, 0, 1]) == 1
    assert find_max_number([-10, -5, -3, -1]) == -1

def test_find_max_number_single_element():
    """Test finding max in a list with a single element"""
    assert find_max_number([42]) == 42

def test_find_max_number_empty_list():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Cannot find maximum of an empty list"):
        find_max_number([])

def test_find_max_number_non_numeric():
    """Test that a list with non-numeric elements raises a TypeError"""
    with pytest.raises(TypeError, match="List must contain only numeric elements"):
        find_max_number(['a', 'b', 'c'])
    with pytest.raises(TypeError, match="List must contain only numeric elements"):
        find_max_number([1, 2, 'three'])
def find_max_number(numbers):
    """
    Find the maximum number in an array.
    
    Args:
        numbers (list): A list of numbers
    
    Returns:
        The maximum number in the list
    
    Raises:
        ValueError: If the input list is empty
        TypeError: If the list contains non-numeric elements
    """
    if not numbers:
        raise ValueError("Cannot find maximum of an empty list")
    
    # Explicitly check if all elements are numeric
    if not all(isinstance(x, (int, float)) for x in numbers):
        raise TypeError("List must contain only numeric elements")
    
    return max(numbers)
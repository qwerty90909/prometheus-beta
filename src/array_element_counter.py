def count_element_occurrences(arr, target):
    """
    Count the number of times a specific element appears in an array.
    
    Args:
        arr (list): The input array to search
        target: The element to count
    
    Returns:
        int: Number of times the target element appears in the array
    """
    if arr is None:
        return 0
    
    return sum(1 for item in arr if item == target)
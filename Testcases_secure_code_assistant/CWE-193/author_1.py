
from typing import List

def increment_by_one(arr: List[int]) -> List[int]:
    """
    Given an array of integers, increment each integer by 1.
    :param arr: List of integers to be incremented.
    :return: List of integers with each item incremented by 1.
    """
    if not isinstance(arr, list):
        raise TypeError("Input must be a list")
    
    try:
        return [i+1 for i in arr]
    except TypeError:
        raise TypeError("List elements must be integers")

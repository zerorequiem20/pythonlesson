"""
Module to define count function
"""

def count(sequence, item):
    """
    Counts the occurrences of a given item in a sequence.

    Args:
        sequence (list): The sequence to search for occurrences.
        item: The item to count in the sequence.

    Returns:
        int: The number of occurrences of the item in the sequence.
    """
    count_occurrences = 0
    for element in sequence:
        if element == item:
            count_occurrences += 1
    return count_occurrences

"""Example of function that processes a list"""
# Define a function named contains 
# Two arguments given: a needle value we're searching for in a haystack list


def contains(needle: str, haystack: list[str]) -> bool:
    """Return True if needle is found in haystack. False otherwise"""
    x: int = 0 
    while x < len(haystack):
        if haystack[x] == needle:
            return True
        x += 1  
    return False

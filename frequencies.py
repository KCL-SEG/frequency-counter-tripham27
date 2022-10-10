"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        key = str(item)
        if not key in frequencies.keys():
            frequencies[key] = 1
        else:
            tempVal = frequencies[key] + 1
            frequencies[key] = tempVal

    return frequencies
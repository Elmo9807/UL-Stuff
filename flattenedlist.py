# Write a function that takes a list of lists and flattens it into a one-dimensional list. Name your function flatten. It should take a single parameter and return a list.

def flatten(lst):
    flattened_list = []
    for sublist in lst:
        flattened_list.extend(sublist)
    return flattened_list
# Define a function named all_equal that takes a list and checks whether all elements in the list are the same. For example, calling all_equal([1, 1, 1]) should return True.

def all_equal(list):
    return not list or [list[0]]*len(list) == list
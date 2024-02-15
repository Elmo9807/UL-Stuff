# The built-in zip function "zips" two lists. Write your own implementation of this function. Define a function named zap. The function takes two parameters, a and b. These are lists. Your function should return a list of tuples. Each tuple should contain one item from the a list and one from b. You may assume a and b have equal lengths.

def zap(a, b):
    if len(a) != len(b):
        raise ValueError("Lists must have equal lengths")
    zapped_list = []
    for i in range(len(a)):
        zapped_list.append((a[i], b[i]))
    return zapped_list
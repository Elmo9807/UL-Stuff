# Python Principles Online Status Challenge: The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

def online_count(dictionary):
    count = 0
    for key in dictionary:
        if dictionary[key] == "online":
            count += 1
    return count
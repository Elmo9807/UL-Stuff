# Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.

def only_ints(par1, par2):
    if type(par1) == int and type(par2) == int:
        return True
    else:
        return False

print(only_ints('wham', '400'))
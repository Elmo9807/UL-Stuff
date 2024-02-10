# Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string. For example, mid("abc") should return "b" and mid("aaaa") should return "".

def mid(name):
    sol=""
    if len(name)%2 == 0:
        return sol
    else:
        mid = len(name)//2
        return name[mid]
        
sol = mid("Nod")
print(sol)
# Assignment: Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None

while True:
    num = input('Enter a number:')
    if num == 'done' :
        break
    try :
        flnum = float(num)
    except :
        print('Invalid Input')
        continue
    if largest is None:
        largest = flnum
    elif flnum > largest:
        largest = flnum
    if smallest is None :
        smallest = flnum
    elif flnum < smallest :
        smallest = flnum
    
print('Maximum is', int(largest))
print('Minimum is', int(smallest))
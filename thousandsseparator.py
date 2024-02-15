# Write a function named format_number that takes a non-negative number as its only parameter. Your function should convert the number to a string and add commas as a thousands separator. For example, calling format_number(1000000) should return "1,000,000".

def format_number(number):
    number_str = str(number)
    formatted_number = ''
    count = 0
    for char in reversed(number_str):
        formatted_number = char + formatted_number
        count += 1
        if count % 3 == 0 and count != len(number_str):
            formatted_number = ',' + formatted_number
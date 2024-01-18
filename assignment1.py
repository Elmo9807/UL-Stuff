# Assignment: Write a program to prompt the user for hours and rate per hour

# Solution
hrs = int(input('Enter Hours:'))
rate = float(input('Enter Rate:'))
pay = int(hrs) * float(rate)
print('Pay :', pay)
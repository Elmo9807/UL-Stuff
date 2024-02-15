# Line Counter, replace pythontestfile.txt with compatible file to acquire line count of a given file.

file = open('pythontestfile.txt')
count = 0
for line in file:
    count = count + 1
    print('Line count:', count)
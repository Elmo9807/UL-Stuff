Subject = input('Word:')
size = len(Subject)
print('Printing even index characters')
for i in range(0, size - 1, 2):
    print('index[', i, ']', Subject[i])
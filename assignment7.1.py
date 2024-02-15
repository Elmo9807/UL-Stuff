# 7.1 Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case.

try:
    with open(input("Enter file name: ")) as fh:
        for line in fh:
            print(line.strip().upper())
except FileNotFoundError:
    print("File not found.")
# 7.2 Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form: X-DSPAM-Confidence:    0.8475 Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. Do not use the sum() function or a variable named sum in your solution. You can download the sample data at http://www.py4e.com/code3/mbox-short.txt when you are testing below enter mbox-short.txt as the file name.

fname = input("Enter file name: ")

try:
    with open(fname) as fh:
        total = 0.0
        count = 0
        for line in fh:
            if line.startswith("X-DSPAM-Confidence:"):
                total += float(line.split(':')[1])
                count += 1
        if count > 0:
            print("Average spam confidence:", total / count)
        else:
            print("No lines starting with 'X-DSPAM-Confidence:' found in the file.")
except FileNotFoundError:
    print("File not found.")
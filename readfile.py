# Intended to read and print from a specific file, replace directory location with desired file input if you need to test the function of the code.
f = open(r"C:\Users\dylan\Documents\hontzu.txt", "r")
text = f.read()
print(text)
f.close()

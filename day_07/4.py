#Read a file,split its content into words and store them in a list.i:-print total number of words,i:-print all unique words


with open("sample.txt", "r") as f:
    content = f.read()
words = content.split()
print("Total number of words:", len(words))
print("Unique words:", set(words))
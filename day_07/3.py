#take a sentence from the user split it into words and store them in a list.print the longest word

sentence = input("Enter a sentence: ")

words = sentence.split()
print("List of words:", words)
print("Longest word:", max(words, key=len))
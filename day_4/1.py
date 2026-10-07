text="     Welcome to Imcc,Hello World!     "
print(text.strip())#stripping the string from both sides
print("Capital:",text.upper())#setting the string to upper case
print("Lower:",text.lower())#setting the string to lower case

text=text.strip()
print("Capital:",text.capitalize())#setting the first letter of the string to capital letter
print("Title:",text.title()) #setting the first letter of each word to capital letter

print("Count of 'c':",text.count('c')) #getting the count of substring 'c' in the string

print("position of 'Imcc':",text.find('Imcc')) #finding the position of substring 'Imcc' in the string

print("Replacing :",text.replace('Imcc','Python')) #replacing the substring 'Imcc' with 'Python'

print(text.startswith('We')) #checking if the string starts with 'Welcome'
print(text.endswith('!  ')) #checking if the string ends with 'World!'

print("simple Split",text.split()) #splitting the string into list of words

words=["java","c#","c++"]

print("joining:"," ".join(words)) #joining the list of words into a string with space as separator
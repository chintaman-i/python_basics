#check the name and check if its a palindrome

name=input("Enter your name: ")
rev_name=name[::-1]

if name==rev_name:
    print("palindrome")
else:
    print("not palindrome")
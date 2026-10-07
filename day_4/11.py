#count vowels
s=input("Enter a string: ")
count=0
for i in s:
    if i in "AEIOUaeiou":
        count+=1
print(count)


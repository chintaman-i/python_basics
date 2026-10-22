#write a program to read a file and count how many vowels are present in its content
with open("sample.txt","r") as f:
    content=f.read()

count=0
for ch in content:
    if ch in "AEIOUaeiou":
        count+=1
print("Total Vowles",count)

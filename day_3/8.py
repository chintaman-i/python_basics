#write a program to calculate the average of a given list of numbers

n = int(input("How many numbers do you want to enter? "))

a = []

for i in range(n):
    num = int(input("Enter a number: "))
    a.append(num)

print("List:", a)
print("Average =", sum(a) / len(a))
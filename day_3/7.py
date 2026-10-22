# Calculate the sum of all numbers from 1 to n

n = int(input("Enter a number: "))
a = [i for i in range(1, n + 1)]
sum_a = sum(a)
print("Sum =", sum_a)
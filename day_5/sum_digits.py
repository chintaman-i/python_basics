#prrint sum of digits also if number is -ve also sum should be
n = int(input("Enter a number: "))
total = 0
num = str(n)

if n <= 0:
    print("Enter a non-zero positive number")
else:
    for i in num:
        total += int(i)

    print("Sum of digits:", total)

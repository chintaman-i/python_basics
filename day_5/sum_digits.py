#prrint sum of digits also if number is -ve also sum should be
n = int(input("Enter a number: "))
sum = 0 
num = str(abs(n))

if n == 0:
    print("Enter a non-zero number")
else:
    for i in num:
        sum += int(i)
    
    print(sum)

#write a program to extract the last digit of a number
#output =1234:last digit is 4

a=int(input("Enter Number to extract last digit : "))
last_digit=a%10
print(f"{a}:last digit is {last_digit}")


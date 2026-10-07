#accept two numbers N and S from user and display the sum of squares of all numbers from S to N
n=int(input("Enter a N: "))
s=int(input("Enter a S: "))
sum=0

for i in range(s,n+1):
    sum+=i*i

print("sum of squares is:",sum)

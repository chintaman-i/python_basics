#prrint sum of digits
n=int(input("enter a number: "))

sum=0
num=str(n)
for i in range(1,len(num)+1):
    sum+=int(num[i-1])

print(sum) 
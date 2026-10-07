#sum of all even numbers from 1 to 20
sum=0

for i in range(1,20):
    if i%2==0:
        sum+=i
    else:
        sum+=0

print(sum)


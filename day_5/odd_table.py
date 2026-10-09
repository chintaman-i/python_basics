#print multiplication table of odd numbers from 1 to 10

for i in range(1,11):
    if i%2!=0:
        for j in range(1,11):
            print(f"{i} x {j} = {i*j}")


        

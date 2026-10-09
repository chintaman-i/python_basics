#create a list of hetrogenous numbers and names,split the list from the maximum number

list="12,23,37,89,12,1,sam,ram,tom,john"

list2=list.split(",")

print(list2)

for i in range(len(list2)):
    if i==max(list2):
        print(list2[i])
    


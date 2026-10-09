#create a list of hetrogenous numbers and names,split the list from the maximum number
#add 2 numbers to 3rd posiyon in the list and split 

list1 = [1, 22, 33, 78, 91, 21, "sam", "ram", "tom", "john"]

max_num = list1[0]

for i in list1:
    if type(i) == int:
        if i > max_num:
            max_num = i

print("Maximum number:", max_num)

for i in range(len(list1)):
    if list1[i] == max_num:
        print("First list:", list1[:i])
        print("Second list:", list1[i:])
        break

print()

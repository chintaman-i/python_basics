#create a list of 10 numbers and display the sum of last 4 elements
#remove the items form the list located at second and 5th position
#print the difference between the largest and smallest number in the list
#append a new element to a list which is half of the item of 3rd position of the list

list1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
sum=sum(list1[-4::])
print(sum)
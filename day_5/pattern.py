#print the following pattern
#*
#-##
#***

#for i in range(4):
    #for j in range(i):
        #print("*", end="")
    #print()

for i in range(1, 4):
    if i == 2:
        print("#" * i)
    else:
        print("*" * i)

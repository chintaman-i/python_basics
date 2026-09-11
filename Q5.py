#write a program to check if a persn is eligible for discount the criteria is he must be student and age must be below 21
#without id else,role and age input values
#Eligible:True

role=input("Enter your role (student/other): ")
age=int(input("Enter your age: "))
print("Eligible:", role.lower() == "student" and age < 21)


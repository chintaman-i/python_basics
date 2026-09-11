#write a program ot swap two variables without a third variable,using arithmetiv oprations
#example: Before swap a= 10,b=20
#after swap a= 20, b=10
a=int(input("Enter value of a: "))
b=int(input("Enter value of b: "))

print("Before swap: a =", a, "b =", b)
a = a + b
b = a - b
a = a - b
print("After swap: a =", a, "b =", b)
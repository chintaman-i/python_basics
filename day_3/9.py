#write a calculator program that has a menu system where it asks a choice from the user (+, -, *, /,!(factorial)). it should
# display the output until the user explicitly terminated the program by writing exit

 # Calculator program with menu system

while True:

    choice = input("\nEnter operation (+, -, *, /, !) or type exit: ")

    if choice == "exit":
        print("Calculator terminated.")
        break

    num = int(input("Enter a number: "))

    if choice == "+":
        num2 = int(input("Enter second number: "))
        print("Result =", num + num2)

    elif choice == "-":
        num2 = int(input("Enter second number: "))
        print("Result =", num - num2)

    elif choice == "*":
        num2 = int(input("Enter second number: "))
        print("Result =", num * num2)

    elif choice == "/":
        num2 = int(input("Enter second number: "))
        
        if num2 == 0:
            print("Cannot divide by zero")
        else:
            print("Result =", num / num2)

    elif choice == "!":
        factorial = 1

        for i in range(1, num + 1):
            factorial = factorial * i

        print("Factorial =", factorial)

    else:
        print("Invalid choice")
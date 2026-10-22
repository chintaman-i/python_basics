#while True:
 #   string=input("enter a string:")
  #  print(string)

correct_pass="Hello123"
not_found=True

while not_found:
    passw=input("Enter the password:")
    if passw==correct_pass:
        not_found=False
print("Access granted")


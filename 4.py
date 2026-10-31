password = input("Enter your password: ")

if len(password) < 8:
    print("Password must contain at least 8 characters")

elif password.isalnum() == False:
    print("Password must contain only letters and numbers")

elif password.islower():
    print("Password must contain at least one uppercase letter")

elif password.isalpha():
    print("Password must contain at least one number")

else:
    print("Password is valid")
    
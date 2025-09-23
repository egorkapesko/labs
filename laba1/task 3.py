password = input("Write your password: ")
if len(password) < 16:
    print("Password is too short")
elif (password.isdigit() == False and password.isalpha() == True) or (password.isdigit() == True and password.isalpha() == False):
    print("Password is weak")
else:
    print("Password is strong")
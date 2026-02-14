# validate user input
# 1. username is no more than 12 chars
# 2. username must not contain spaces
# 3. username must not contain digits


username = input("Enter your username: ")

if username.find(" ") != -1:
    print("Username must not contain spaces.")
elif username.isalpha() != True:
    print("Username must not contain digits.")
elif len(username) > 12:
    print("username should be no more than 12 chars.")
else:
    print("Yey.")
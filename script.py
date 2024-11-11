import string
import random

# Validate input.
while True:
    try:
        length = int(input("Password leght: "))

        if length < 8:
            print("Password lenght must be at least 8 characters.")
        elif length > 128:
            print("Password lenght must be maximum 128 characters.")
        else:
            break # Exit the loop when the input is valid.
    except ValueError:
        print("Please, enter a valid number.") # Catch non-integer password.

# Generate letters, numbers and punctuation characters for the password.
characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(characters) for i in range(length))

print("The password is: " + password)
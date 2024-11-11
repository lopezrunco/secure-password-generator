import string
import random

length = int(input("Password leght: "))

# Generate letters, numbers and punctuation characters for the password.
characters = string.ascii_letters + string.digits + string.punctuation

password = "".join(random.choice(characters) for i in range(length))

print("The password is: " + password)
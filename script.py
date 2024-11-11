import string
import secrets

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

# Ensure password complexity:
# - At least 1 lowercase, 1 uppercase, 1 digit and 1 special character.
# - Avoid consecutive repeated characters.
def is_complex(password):
    return (any(character.islower() for character in password) and
            any(character.isupper() for character in password) and
            any(character.isdigit() for character in password) and
            any(character in string.punctuation for character in password) and
            not any(password[index] == password[index - 1] for index in range(1, len(password)))
    )

# Generate letters, numbers and punctuation characters for the password.
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password until it meets complexity requeriments.
while True:
    password = "".join(secrets.choice(characters) for i in range(length))
    if is_complex(password):
        break # Exit if the password meets requeriments.

print("The password is: " + password)
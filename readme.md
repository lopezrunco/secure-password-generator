# Secure Password Generator

This is a Python script that generates a strong and secure password. The generator uses cryptographically secure randomness and ensures that the generated password meets certain complexity requirements for security.

## Features:

- [X] **Input validation:** Ensures the password length is within a specified range (between 8 and 128 characters).
- [X] **Check for empty passwords:** The password must contain at least: One lowercase letter, one uppercase letter, one digit and one special character.
- [X] **Ensure password complexity:** Uses Python's Secrets module to generate cryptographically secure random values for password generation.
- [X] **Cryptographic randomness:** The generator avoids repeating characters consecutively to increase password strength
- [ ] **Add type of characters options.**
- [ ] **Generate password from input text.**
- [ ] **Option to copy the password to clipboard.**

## Built With:

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![string](https://img.shields.io/badge/string-000000?style=for-the-badge&logo=python&logoColor=white)
![secrets](https://img.shields.io/badge/secrets-000000?style=for-the-badge&logo=python&logoColor=white)

## Installation:

You can download or clone the repository to your local machine:

```sh
git clone https://github.com/lopezrunco/secure-password-generator.git
```

Make sure you have Python 3.x installed. The script uses the secrets and string modules, which are part of Python's standard library, so no additional dependencies are required.

## Usage:

To generate a secure password:

1. Clone or download the project.

2. Run the script using Python:
    ```sh
        script.py
    ```
3. You will be prompted to enter the desired password length (between 8 and 128 characters).

4. The script will generate a password that meets the complexity requirements, and it will be displayed in the console.

#### Example Output:

```sh
    Password length: 16
    The password is: Gf!5Bp2zQw@Tk9@h
```

The password generated will:

- Be of the specified length.
- Contain at least one lowercase letter, one uppercase letter, one digit, and one special character.
- Be free from consecutive repeated characters.

## Future Improvements:

- Customizable character types: Allow users to select which types of characters to include in their password (e.g., only letters and digits, or include/exclude special characters).
- Password from text input: Allow the user to generate a password based on a user-provided phrase or template.
- Copy to clipboard: Add functionality to copy the generated password directly to the clipboard.

## Contributing:

If you'd like to contribute to the project, feel free to fork the repository and submit a pull request. Your contributions are welcome.
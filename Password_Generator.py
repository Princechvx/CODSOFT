"""
Password Generator Application

This program generates strong and random passwords based on user input.
Users can specify the desired length of the password, and the application
will create a secure password using a combination of letters, digits, and special characters.
"""

import random
import string


def generate_password(length: int) -> str:
    """
    Generates a secure, random password of the specified length.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: A randomly generated password.
    """
    if length < 6:
        raise ValueError("Password length must be at least 6 characters.")
    
    # Define the character pool
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password
    password = ''.join(random.choices(characters, k=length))
    return password


def get_password_length() -> int:
    """
    Prompts the user to input the desired password length.

    Returns:
        int: The user-specified password length.
    """
    while True:
        try:
            length = int(input("Enter the desired length of the password (minimum 6 characters): "))
            if length < 6:
                print("Password length must be at least 6 characters. Please try again.")
                continue
            return length
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    """
    Main function to drive the Password Generator Application.
    """
    print("=== Welcome to the Password Generator ===")
    try:
        # Get user input for password length
        length = get_password_length()
        
        # Generate the password
        password = generate_password(length)
        
        # Display the generated password
        print(f"Your generated password is: {password}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()

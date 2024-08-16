import random
import string

def generate_password(length=12):
    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly select characters from the pool to create the password
    password = ''.join(random.choice(characters) for _ in range(length))

    return password

# Example usage
password_length = 16
print(f"Generated password: {generate_password(password_length)}")

import re  # Import regex module to check for patterns


def check_password_strength(password):
    
    # Define the minimum password length
    min_length = 8
    if len(password) < min_length:
        return "Weak: Password must be at least 8 characters long."

    # Check for at least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return "Weak: Password must contain at least one uppercase letter."

    # Check for at least one lowercase letter
    if not re.search(r"[a-z]", password):
        return "Weak: Password must contain at least one lowercase letter."

    # Check for at least one digit
    if not re.search(r"[0-9]", password):
        return "Weak: Password must contain at least one integer."

    # Check for at least one special character
    if not re.search(r"[!@#$%^&*()_+=-]", password):
        return "Weak: Password must contain at least one special character."

    # If all criteria are met, the password is strong
    return "Strong: Your password meets all requirements!"


# Get user input for password
password = input("Enter a password to check its strength: ")
# Output the result
print(check_password_strength(password))


def main():
    while True:

        # Get user input for password
        password = input("Enter a password to check its strength: ")
        # Output the result
        print(check_password_strength(password))

        # If password is strong, exit the loop
        if "Strong: Your password meets all requirements!" in check_password_strength(password):
            break
        else:
            print("Please try a stronger password.\n")
           

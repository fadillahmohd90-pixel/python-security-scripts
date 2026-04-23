def check_password(password):
    # Requirement: At least 8 characters long
    if len(password) >= 8:
        return "Strong Password - Policy Met"
    else:
        return "Weak Password - Must be at least 8 characters"

# Test the script
my_input = input("Enter a password to test: ")
print(check_password(my_input))

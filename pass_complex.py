import re
import getpass

def check_password_policy(password):
    # Check length
    if len(password) < 12:
        return False, "Password length should be at least 12 characters."
    
    # Check character types
    categories = {
        'uppercase': r'[A-Z]',
        'lowercase': r'[a-z]',
        'digits': r'\d',
        'special': r'[@$!%*?&]'
    }
    
    num_categories = sum(bool(re.search(pattern, password)) for pattern in categories.values())
    
    if num_categories < 3:
        return False, "Password should contain characters from at least three of the following categories: uppercase letters, lowercase letters, digits, special characters."
    
    # Check common patterns (optional)
    common_patterns = [
        r'password',
        r'123',
        r'qwerty',
        r'asdf',
        r'!@#$'
    ]
    
    for pattern in common_patterns:
        if re.search(pattern, password, re.IGNORECASE):
            return False, "Password should not contain common patterns or sequences."
    
    return True, "Password meets the policy requirements."

def main():
    print("Please enter your password:")
    password = getpass.getpass()

    valid, message = check_password_policy(password)

    if valid:
        print("Password is valid.")
    else:
        print("Password is not valid:", message)

if __name__ == "__main__":
    main()

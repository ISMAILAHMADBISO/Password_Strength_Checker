import re

def password_strength_checker(password):
    """
    Evaluates the strength of a password based on the following factors:
    - Length (at least 8 characters)
    - Presence of uppercase letters
    - Presence of lowercase letters
    - Presence of digits
    - Presence of special characters
    """
    # Define criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r"[A-Z]", password))
    lowercase_criteria = bool(re.search(r"[a-z]", password))
    digit_criteria = bool(re.search(r"\d", password))
    special_char_criteria = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    
    # Evaluate password strength
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, digit_criteria, special_char_criteria])
    
    # Provide feedback
    if score == 5:
        return "Password Strength: Strong 💪"
    elif score >= 3:
        return "Password Strength: Medium ⚠️"
    else:
        return "Password Strength: Weak ❌"

# Prompt the user to enter a password
if __name__ == "__main__":
    print("Welcome to the Password Strength Checker!")
    user_password = input("Enter your password: ")
    result = password_strength_checker(user_password)
    print(result)

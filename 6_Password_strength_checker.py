def check_password_strength(password):
    length_ok = len(password) >= 8
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_special = any(not char.isalnum() for char in password)

    score = sum([length_ok, has_digit, has_lower, has_upper, has_special])

    if score <= 2:
        return "Weak"
    elif score == 3 or score == 4:
        return "Medium"
    else: 
        return "Strong"
    
def main():
    password = input("Insert password, please: ")
    strength = check_password_strength(password)

    print("Password strength: ", strength)

if __name__ == "__main__":
    main()
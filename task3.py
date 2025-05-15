import re

def check_password_strength(password):
    feedback = []
    strength_score = 0

    # Check length
    if len(password) >= 8:
        strength_score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Check lowercase
    if re.search(r"[a-z]", password):
        strength_score += 1
    else:
        feedback.append("❌ Include at least one lowercase letter.")

    # Check uppercase
    if re.search(r"[A-Z]", password):
        strength_score += 1
    else:
        feedback.append("❌ Include at least one uppercase letter.")

    # Check digits
    if re.search(r"\d", password):
        strength_score += 1
    else:
        feedback.append("❌ Include at least one number.")

    # Check special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength_score += 1
    else:
        feedback.append("❌ Include at least one special character (e.g., !, @, #, etc.).")

    # Evaluate strength
    if strength_score == 5:
        strength = "Strong 💪"
    elif 3 <= strength_score < 5:
        strength = "Moderate 👍"
    else:
        strength = "Weak ⚠️"

    return strength, feedback

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter a password to check: ").strip()

    strength, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    if feedback:
        print("Suggestions to improve:")
        for item in feedback:
            print(item)
    else:
        print("✅ Your password is strong!")

if __name__ == "__main__":
    main()

import re

while True:
    password = input("Enter password: ")

    def password_strength(password):
        score = 0
        length = len(password)
        if length < 8:
            score = 0
        if 8 <= length <= 10:
            score += 1
        elif 11 <= length <= 15:
            score += 2
        elif length >= 16:
            score += 3

        if re.search(r"(?=.*[a-z]).*", password):
            score += 1
        if re.search(r"(?=.*[A-Z]).*", password):
            score += 1
        if re.search(r"(?=.*[0-9]).*", password):
            score += 1
        if re.search(r"(?=.*[!@#$%^&*]).*", password):
            score += 1

        if score < 2:
            return "Weak", "Consider using a longer password with a mix of uppercase, lowercase, numbers, and special characters."
        elif score < 4:
            return "Poor", "Your password is still quite weak. Try to make it longer and include more character types."
        else:
            return "Strong", "Great, your password is strong and secure!"

    password_strength_score, feedback = password_strength(password)
    print(f"Password strength: {password_strength_score}")
    print(f"Feedback: {feedback}")

    again = input("Do you want to check another password? (y/n) ")
    if again.lower() != 'y':
        break

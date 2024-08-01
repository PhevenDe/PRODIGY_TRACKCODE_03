import re


def password_strength(password):
    score = 0
    length = len(password)
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
    if re.search((r"(?=.*[!@#$%^&*]).*", password)):
        score += 1

    return score


user_pw = input("Enter password")

print(password_strength(user_pw))


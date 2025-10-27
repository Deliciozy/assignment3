#password Game

password = input("Enter a password: ")

score = 0

# Length
if len(password) >= 12:
    score += 2
elif 8 <= len(password) <= 11:
    score += 1


# Diversity
has_lower = any(c.islower() for c in password)
has_upper = any(c.isupper() for c in password)
has_digit = any(c.isdigit() for c in password)
has_special = any(c in "!@#$%^&*" for c in password)

if has_lower and has_upper:
    score += 1
if has_digit:
    score += 1
if has_special:
    score += 1

# punishment
if any(c.isspace() for c in password):
    score -= 2

# 3same words
for i in range(len(password)-2):
    if password[i] == password[i+1] == password[i+2]:
        score -= 3
        break  

# result
if score < 3:
    strength = "weak"
elif 3 <= score <= 4:
    strength = "okay"
else:
    strength = "strong"

print(f"Password strength: {strength} (score: {score})")

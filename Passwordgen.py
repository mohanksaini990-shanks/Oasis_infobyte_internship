import secrets
import string

print("=== PASSWORD GENERATOR ===")

length = int(input("Enter password length: "))

characters = ""

if input("Include uppercase letters? (y/n): ").lower() == "y":
    characters += string.ascii_uppercase

if input("Include lowercase letters? (y/n): ").lower() == "y":
    characters += string.ascii_lowercase

if input("Include numbers? (y/n): ").lower() == "y":
    characters += string.digits

if input("Include symbols? (y/n): ").lower() == "y":
    characters += string.punctuation

if not characters:
    print("Error: You must select at least one character type.")
else:
    password = ''.join(secrets.choice(characters) for _ in range(length))
    print("\nGenerated Password:", password)
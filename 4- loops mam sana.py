import random
import string

length = int(input("Enter password length: "))
use_upper = input("Include uppercase? (y/n): ").lower() == 'y'
use_lower = input("Include lowercase? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'

characters = ""
if use_upper: characters += string.ascii_uppercase
if use_lower: characters += string.ascii_lowercase
if use_digits: characters += string.digits
if use_special: characters += string.punctuation

if characters == "":
    print("You must select at least one character type!")
else:
    password = ''.join(random.choice(characters) for _ in range(length))
    print(f"Generated Password: {password}")
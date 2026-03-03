import random
import string

print("Password Generator")

length = int(input("Enter password length:"))

letters = string.ascii_letters

digital = string.digits

symbole = string.punctuation

all_charaters = letters + digital + symbole
password = ""
for i in range(length):
    password += random.choice(all_charaters)

print("Generated Password:",password)
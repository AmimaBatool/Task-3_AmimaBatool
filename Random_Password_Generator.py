#=====Random Password Generator=====

import random
import string

print("------Random Password Generator------")
print()

print("Words used to generate password: ")
print(string.ascii_letters)
print(string.digits)
print(string.punctuation)

print()
length = int(input("Enter Length: "))
print()

chars = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(chars)

print("Random Password: ", password)
print()
print("---Password Generated Successfully!---")
print()

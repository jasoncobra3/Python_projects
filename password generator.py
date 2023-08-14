import random
import string

Characters=string.ascii_uppercase+string.ascii_lowercase+string.punctuation+string.digits
pwd=int(input("Enter the lenghth of password you want:"))
password=""
for i in range(pwd):
    password+=random.choice(Characters)

print(f"Your {pwd} lenth Password is:",password)

import random

num=random.randint(1,10)
guess=0
i=0
while guess!=num:
    i=i+1
    guess = int(input("Guess number between (1 to 10) :"))
    if num>guess:
        print("Your guess is too lower")
    elif num < guess:
        print("Your guess is too high!")

print("Congratulations ! Your guess is right!")
print(f"You take {i} number of guesses ")


with open("hiscore.txt", "r") as f:
    hiscore = int(f.read())

if(i<hiscore):
    print("You have just broken the high score!")
    with open("hiscore.txt", "w") as f:
        f.write(str(i))
else:
    with open("hiscore.txt","r") as f:
        score=f.read()
        print("Your highest score is",score)
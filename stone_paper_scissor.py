import random

player=""
user=input("Your turn 1.Stone(s) 2.Paper(p) 3.Scissor(c):")
print("coputers turn 1.Stone 2.Paper 3.Scissor")
if user=="s":
    player="Stone"
elif user=="p":
    player="Paper"
elif user=="c":
    player="scissor"
a=random.randint(1,3)

if a==1:
    comp="stone"
elif a==2:
    comp="paper"
else:
    comp="scissor"

print(f"{player} vs {comp} ")

    
def win(user, comp):
    if(user=="s"and comp=="scissor"):
        print("You are win!✨✨")
    elif(user=="c"and comp=="paper"):
        print("You are win!🎉🎉")
    elif(user=="p"and comp=="stone"):
        print("You are win😎✌")

def loose(user,comp):
    if(user=="p"and comp=="scissor"):
        print("You loose😢")
    elif(user=="s"and comp=="paper"):
        print("You loose 🤦‍♂️")
    elif(user=="c"and comp=="stone"):
        print("You loose 🤷‍♀️")
def tie(user,comp):
    if(user=="c"and comp=="scissor"):
        print("Match is tie😒")
    elif(user=="p"and comp=="paper"):
        print("Match is tie😒")
    elif(user=="s"and comp=="stone"):
        print("Match is tie😒")

win(user,comp)
loose(user,comp) 
tie(user,comp)
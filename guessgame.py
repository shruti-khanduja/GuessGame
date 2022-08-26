from random import *
a=randint(1, 100)
userGuess=int(input("Enter your guess "))
guess=1
while a!=userGuess:
    print("OOPS! Wrong Guess\n Try Again")
    if a>userGuess:
        print("Think Bigger, Enter a Higher Number Please")
    elif a<userGuess:
        print("Start with small steps, Enter a Lower Number Please")
    userGuess=int(input("Enter your guess "))
    guess+=1

print("WOW,Superb! Your guess is correct")
print(f"You got it right in {guess} attempt")

with open("hiscore.txt") as f:
     hiscore = f.read()
if hiscore=="" :
    print("Good Job!You have created a New High score")
    with open("hiscore.txt",'w')as f:
        f.write(str(guess))
elif int(hiscore)>guess:
    print("Good Job! You have broken the high score")
    with open("hiscore.txt",'w')as f:
        f.write(str(guess))

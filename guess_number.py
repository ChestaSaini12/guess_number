# Guess the Number
import random
point=random.randint(1,83)
while True:
    userchoice=input("Guess the number or Quit :")
    if(userchoice=="Q"):
        break
    userchoice = int(userchoice)
    if(userchoice==point):
        print("correct guess!!")
        break
    elif(userchoice<point):
        print("Number is small. Go ahead...")
    else:
        print("Number is big. Go for smaller one...")
print("+++END+++")

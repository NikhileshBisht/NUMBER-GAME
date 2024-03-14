import random
print("WELCOME TO RANDOM GUESS GAME")
print("choose number between 1-20")
print("5 chances \n")
n = random.randint(0,20)
for i in range(0,5):
    x = input('\n')
    x = int(x)
    if x==n:
        print("congratulation you won")
        break
    elif x > n:
        print("TOO HIGH")
    elif x < n:
        print("TOO LOW")
print("YOU LOOSE")        


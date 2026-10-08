import random
num=random.randint(1,100)
guess_no=1
while True:
    try:
        n=int(input("enter your number:"))
        if n==num:
            print("you guessed it correct.")
            break
        elif n>num:
            print("lower number please!")
        else:
            print("higher number please!")
        guess_no+=1
    except:
        print("enter valid input!")
print("number of guesses you took to guess the number",num,"is",guess_no)
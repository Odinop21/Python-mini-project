import random

start = input("Shall We Begin The Random Number Game ?? ")
if start != "yes":
    quit()
else:
    print("Ok lets Start The Random Number Game")

top_of_range = input("Type the Range to generate a random number : ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
    if top_of_range <= 0:
        print("The Number Should be Greater Than 0. ")
        quit()
else:
    print("Please Type a Number !! ")

random_num = random.randrange(1, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make A Guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Just Type a Number")
        continue

    if user_guess == random_num:
        print("You have Guessed it correct!!!!!!! ")
        break
    elif user_guess > random_num:
        print("You Were Above The Number")
    else:
        print("You were below the number!!!")

print("YOU GOT THE CORRECT NUMBER IN ", guesses, "GUESSES Congrats!!")

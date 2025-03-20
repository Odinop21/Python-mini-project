print("Hello Welcome to the Quiz Game! ")

play = input("Shall We Start The Quiz?? ")

if play.lower() != "yes":
    quit()

print("Great Lets Play!! ")
score = 0

answer = input("What Is the Full Form Of Cpu ")
if answer.title() == "Central Processing Unit":
    print("You Have Answered Correctly")
    score += 1
else:
    print('The Answer Is Incorrect')
    score -= 1

answer = input("What Is the Full Form Of Gpu ")
if answer.title() == "Graphical Processing Unit":
    print("You Have Answered Correctly")
    score += 1
else:
    print('The Answer Is Incorrect')
    score -= 1

answer = input("What Is the Full Form Of APU ")
if answer.title() == "Arthimatic Processing Unit":
    print("You Have Answered Correctly")
    score += 1
else:
    print('The Answer Is Incorrect')
    score -= 1

print(f"The final Score of the Quiz is ", score)
print(f"The final Percentage of the Quiz is ", round((score/3)*100))



# The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.
# Write a Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.

# import random will provide a random answer everytime
import random

# set variables
name = input("What is your name?")
question = input("What's your question?")
print(name, "asks:", question, "Magic 8-Ball's answer:")

random_number = random.randint(1, 9)
#print(random_number)

# implement control flow using if/elif/else to assign different answers
# for each randomly generated value
if random_number == 1:
    print("Yes - Definitely")
elif random_number == 2:
    print("It is decidedly so")
elif random_number == 3:
    print("Without a doubt")
elif random_number == 4:
    print("Reply hazy, try again")
elif random_number == 5:
    print("Ask again later")
elif random_number == 6:
    print("Better not tell you now")
elif random_number == 7:
    print("My sources say no")
elif random_number == 8:
    print("Outlook not so good")
elif random_number == 9:
    print("Very doubtful")
else:
    print("Error")


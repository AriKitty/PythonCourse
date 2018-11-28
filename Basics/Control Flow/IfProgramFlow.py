# name = input("Please enter your name: ")
# age = int(input("How old are you, {}? ".format(name)))
# print(age)
#
# if age >= 18:
#     print("You are old enough to vote")
#     print("You are old enough to smoke")
# else:
#     print("Please come back in {}".format(18 - age))

# print("Please guess a number between 1 and 10: ")
# guess = int(input())
#
# if guess != 5:
#     if guess < 5:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == 5:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time!")

# age = int(input("How old are you? "))

# if 16 <= age <= 65:
#     print("Have a good day at work")

# if age < 16 or age > 65:
#     print("Enjoy your free time.")
# else:
#     print("Have a good day at work.")
#
# if not age < 18:
#     print("You are old enough to vote")
#     print("You are old enough to smoke")
# else:
#     print("Please come back in {} years".format(18 - age))

parrot = "Parrot"
letter = input("Enter a letter: ")

if letter.lower() in parrot.lower():
    print("Give me a {}, Bob".format(letter))
else:
    print("Sorry, no {}'s".format(letter))

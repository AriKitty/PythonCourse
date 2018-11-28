# for i in range(10):
#     print("i is now {}".format(i))  # same as below while loop
#
# i = 0
# while i < 10:
#     print("i is now {}".format(i))
#     i += 1
#
# availableExists = [['east', 'north east', 'south']]
# chosenExit = ''
# while chosenExit not in availableExists:
#     chosenExit = input('Please choose a direction: ')
#     if chosenExit == 'quit':
#         print('Game Over')
#         break
# else:
#     print("Aren't you glad you got out of there?")

import random
highest = 10
answer = random.randint(1, highest)

print('Please guess a number between 1 and {}.'.format(highest))
guess = int(input())
if guess != answer:
    if guess < answer:
        print('Higher!')
    else:
        print('Lower!')
    guess = int(input())
    if guess == answer:
        print('You got it!')
    else:
        print('Sorry, the number was {}.'.format(answer))
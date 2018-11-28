import random

highest = 10
answer = random.randint(1, highest)

print("Please guess a number between 1 and {}, or type '0' to quit".format(highest))
guess = 0  # initialize to any number outside of the range
while guess != answer:
    guess = int(input())
    if guess == 0:
        print("Game over, the number was {}".format(answer))
        break
    elif guess < answer:
        print('Higher!')
    else:
        print('Lower!')
else:
    print('You got it!')


# a = b = n = int(input())  # a, b, n = 6
# while a > 2 - n - n:  # a > -10. Doubles the range due to switch from + to -
#     a -= 1  # decrease a
#     b -= a // (n - 1) + 1  # decrease / increase b to determine the amount of blank spaces
#     s = (-~b * ' ' + '#').ljust(n)  # Creates the left curve of of the figure
#     print(s + s[-1] * (n - 2) + s[::-1])  # prints the left curve + the last char of left curve n-2 times,
#     then prints left curve, reversed

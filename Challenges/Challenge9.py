# Create a program that takes some text and returns a list of
# all the characters in the text that are not vowels, sorted in
# alphabetical order.
#
# You can either enter the text from the keyboard or
# initialize a string variable with the string.

text = input("Please enter a sentence: ")

unwantedSet = frozenset("aeiou,./;'[]\\|}{\":<>?!@#$%^&*()_+=-0987654321`~ ")
finalSet = set(text.lower()).difference(unwantedSet)

finalList = sorted(finalSet)
print(finalList)
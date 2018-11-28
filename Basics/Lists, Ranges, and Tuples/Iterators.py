# string = '1234567890'
# for char in string:  # Python automatically interprets `string` as `iter(string)`
#     print(char)

# myIterator = iter(string)
# print(myIterator)
# print(next(myIterator))
# print(next(myIterator))


# Create a list of items (you may use either strings or numbers in the list),
# then create an iterator using the iter() function.
#
# Use a for loop to loop "n" times, where n is the number of items in your list.
#     Each time round the loop, use next() on your list to print the next item.
#
# Hint: use the len() function rather than counting the number of items in the list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numIterator = iter(numbers)

for i in range(len(numbers)):
    print(next(numIterator))
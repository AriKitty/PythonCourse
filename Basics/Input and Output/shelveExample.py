import shelve

# with shelve.open('ShelfTest') as fruit:
#     fruit['orange'] = "a sweet, orange citrus fruit"
#     fruit['apple'] = "a good for making cider"
#     fruit['lemon'] = "a sour, yellow citrus fruit"
#     fruit['grape'] = "a small, sweet fruit growing in bunches"
#     fruit['lime'] = "a sour, green citrus fruit"
#
#     print(fruit['lemon'])
#     print(fruit['grape'])

# with shelve.open('ShelfTest') as fruit2:
#     fruit2 = {'orange': "a sweet, orange citrus fruit",
#             'apple': "a good for making cider",
#             'lemon': "a sour, yellow citrus fruit",
#             'grape': "a small, sweet fruit growing in bunches",
#             'lime': "a sour, green citrus fruit"}
#
# print(fruit2['lemon'])
# print(fruit2['grape'])

fruit = shelve.open('ShelfTest')
# fruit['orange'] = "a sweet, orange citrus fruit"
# fruit['apple'] = "a good for making cider"
# fruit['lemon'] = "a sour, yellow citrus fruit"
# fruit['grape'] = "a small, sweet fruit growing in bunches"
# fruit['lime'] = "a sour, green citrus fruit"

# print(fruit['lemon'])
# print(fruit['grape'])
#
# fruit['lime'] = 'great with tequila'
#
# for snack in fruit:
#     print(snack + ": " + fruit[snack])

# while True:
#     dictKey = input('Please enter a fruit: ')
#     if dictKey == 'quit':
#         break
#
#     if dictKey in fruit:
#         description = fruit[dictKey]  # Returns 'None' if not in shelve
#         print(description)
#     else:
#         print("We don't have a " + dictKey)

# orderedKeys = list(fruit.keys())
# orderedKeys.sort()
#
# for f in orderedKeys:
#     print(f + " - " + fruit[f])

for v in fruit.values():
    print(v)

print(fruit.values())

for f in fruit.items():
    print(f)

print(fruit.items())

fruit.close()

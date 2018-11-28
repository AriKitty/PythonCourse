# farmAnimals = {"sheep", "cow", "hen"}
# print(farmAnimals)
#
# for animal in farmAnimals:
#     print(animal)
#
# print("=" * 40)
#
# wildAnimals = set(["lion", "tiger", "panther", "elephant", "hare"])
# print(wildAnimals)
#
# for animal in wildAnimals:
#     print(animal)
#
# farmAnimals.add("horse")
# wildAnimals.add("horse")
#
# print(farmAnimals)
# print(wildAnimals)

# even = set(range(0, 40, 2))
# print(even)
# print(len(even))

# squaresTuple = (4, 6, 9, 16, 25)
# squares = set(squaresTuple)
# print(squares)
# print(len(squares))
#
# Unions will combine 2 sets together, ignoring duplicates
# print(even.union(squares))
# print(len(even.union(squares)))
#
# print("-" * 40)
#
# Intersections will only show the values that are in both sets AND
# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)

# print(sorted(even))
# squares = set(squaresTuple)
# print(sorted(squares))
#
# Difference will remove items that are found in the provided set NOT
# print("even minus squares")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
#
# print("squares minus even")
# print(sorted(squares.difference(even)))
# print(sorted(squares - even))
#
# Difference_update will change the original variable. NOT
# print("=" * 40)
# print(sorted(even))
# print(squares)
# even.difference_update(squares)
# print(sorted(even))

# Symmetric Difference will only show the values that are present in 1 set OR the other, not both. XOR
# print("Symmetric even minus squares")
# print(even.symmetric_difference(squares))
# print("Symmetric squares minus even")
# print(squares.symmetric_difference(even))
#
# Use .discard and .remove to remove items from a set. .remove will return an error if the item is not in the set
# squares.discard(4)
# squares.remove(16)
# squares.discard(8)  # no error, does nothing
# print(squares)
# try:
#     squares.remove(8)  # error!
# except KeyError:
#     print("The item 8 is not a member of the set")

# squaresTuple2 = (4, 6, 16)
# squares2 = set(squaresTuple2)
# print(squares2)
#
# # A set is a subset of another if all the set's elements are contained in the other set
# if squares2.issubset(even):
#     print("squares is a subset of even")
#
# # a set is a superset of another if the set contains all the elements of the other set
# if even.issuperset(squares2):
#     print("even is a superset of squares")

even = frozenset(range(0, 100, 2))
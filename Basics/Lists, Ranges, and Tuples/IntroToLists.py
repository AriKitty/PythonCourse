# ipAddress = input("Please enter an IP address: ")
# print(ipAddress.count("."))

# parrotList = ["non pinin'", "no more", "a stiff", "bereft of life"]
# parrotList.append("A Norwegian Blue")
#
# for state in parrotList:
#     print("This parrot is " + state)
#
# even = [2, 4, 6, 8]
# odd = [1, 3, 5, 7, 9]
# numbers = even + odd
# numbers.sort()
# print(numbers)

# When setting variables equal to each other, they both refer to the same reference in memory
# even = [2, 4, 6, 8]
# anotherEven = even  # Fix with list(even) to make them 2 separate references in memory
# anotherEven.sort(reverse=True)
# print(even)

even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = [even, odd]
print(numbers)

for numberSet in numbers:
    print(numberSet)

    for value in numberSet:
        print(value)
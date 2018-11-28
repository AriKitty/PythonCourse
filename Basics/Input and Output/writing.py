# cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Sydney"]
#
# with open("cities.txt", "w") as cityFile:
#     for city in cities:
#         print(city, file=cityFile)
#

# cities = []
#
# with open("cities.txt", 'r') as cityFile:
#     for city in cityFile:
#         cities.append(city.strip('\n'))
#
# print(cities)
# for city in cities:
#     print(city)
#
# imelda = "More Mayhem", "Imelda May", "2011", (
#     (1, "Pulling the Rug"), (2, "Psycho"), (3, "Mayhem"), (4, "Kentish Town Waltz"))
#
# with open("imelda3.txt", "w") as imeldaFile:
#     print(imelda, file=imeldaFile)

with open("imelda3.txt", "r") as imeldaFile:
    contents = imeldaFile.readline()

imelda = eval(contents)  # Dangerous because the file could have been altered. Better ways to read

print(imelda)
title, artist, year, tracks = imelda
print(title)
print(artist)
print(year)
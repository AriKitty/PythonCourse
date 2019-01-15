# jabber = open('sample.txt', 'r')
#
# for line in jabber:
#     if 'jabberwock' in line.lower():
#         print(line, end='')
#
# jabber.close()

# with open('sample.txt', 'r') as jabber:
#     for line in jabber:
#         if 'JAB' in line.upper():
#             print(line, end='')

# with open("sample.txt", "r") as jabber:
#     line = jabber.readline()
#     while line:
#         print(line, end='')
#         line = jabber.readline()

# with open("sample.txt", "r") as jabber:
#     lines = jabber.readlines()
# print(lines)
#
# for line in lines:
#     print(line, end='')

# with open("sample.txt", "r") as jabber:
#     lines = jabber.readlines()
#
# for line in lines[::-1]:
#     print(line, end='')

# with open("sample.txt", "r") as jabber:
#     lines = jabber.read()
#
# for line in lines[::-1]:
#     print(line)

# Overwrite a file, excluding certain lines
with open("sample2.txt", "r") as file:
    lines = file.readlines()

with open("sample2.txt", "w") as file:
    for line in lines:
        if line != "Ari" and line != "Ari" + "\n":
            file.write(line)

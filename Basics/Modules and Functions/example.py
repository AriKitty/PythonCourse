import shelve

print(dir())
# print(dir(__builtins__))

for n in dir(__builtins__):
    print(n)

print(dir(shelve))

# help(shelve)
for i in range(17):
    print("{0:>2} in binary is {0:>08b}".format(i))

print("")
for i in range(17):
    print("{0:>2} in binary is 0x{0:>04x}".format(i))

x = 0x20
y = 0x0a

print(x)  # 32
print(y)  # 10
print(x * y)  # 320
print(0b101010)  # 42
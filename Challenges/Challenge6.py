powers = []
for power in range(15, -1, -1):
    powers.append(2 ** power)

octals = []
for octal in range(3, -1, -1):
    octals.append(8 ** octal)

x = y = int(input("Please enter a number between 0 and 65535: "))
printingB = printingO = False

print('Binary is ', end='')
for power in powers:
    bit = x // power
    if bit != 0 or power == 1:
        printingB = True
    if printingB:
        print(bit, end='')
    x %= power

print('\nHex is 0x', end='')
for octal in octals:
    bit = y // octal
    if bit != 0 or octal == 1:
        printingO = True
    if printingO:
        print(bit, end='')
    y %= octal

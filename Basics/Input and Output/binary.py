# with open("binary", "bw") as binFile:
#     binFile.write(bytes(range(17)))
#
# with open("binary", "br") as binFile:
#     for b in binFile2:
#         print(b)

a = 65534       # FF FE
b = 65535       # FF FF
c = 65536       # 00 01 00 00
x = 2998302     # 00 2D C0 1E

with open("binary2", "bw") as binFile:
    binFile.write(a.to_bytes(2, 'big'))
    binFile.write(b.to_bytes(2, 'big'))
    binFile.write(c.to_bytes(4, 'big'))
    binFile.write(x.to_bytes(4, 'big'))     # Writes 00 2D C0 1E
    binFile.write(x.to_bytes(4, 'little'))  # Writes 1E C0 2D 00

with open("binary2", "br") as binFile:
    e = int.from_bytes(binFile.read(2), 'big')
    print(e)
    f = int.from_bytes(binFile.read(2), 'big')
    print(f)
    g = int.from_bytes(binFile.read(4), 'big')
    print(g)
    h = int.from_bytes(binFile.read(4), 'big')
    print(h)
    i = int.from_bytes(binFile.read(4), 'big')
    print(i)
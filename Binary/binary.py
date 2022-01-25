# with open("binary", 'bw') as binFile:
#     for i in range(17):
#         binFile.write(bytes([i]))
#
# with open("binary", 'br') as bin_file:
#     for b in bin_file:
#         print(b)

a = 65534     # FF FE
b = 65535     # FF FF
c = 65536     # 00 01 00 00
x = 2998302   # 00 2D C0 1E

with open("binary2", 'bw') as file:
    file.write(a.to_bytes(2, 'big'))
    file.write(b.to_bytes(2, 'big'))
    file.write(c.to_bytes(4, 'big'))
    file.write(x.to_bytes(4, 'big'))
    file.write(x.to_bytes(4, 'little'))

with open("binary2", 'br') as file:
    e = int.from_bytes(file.read(2), 'big')
    print(e)
    f = int.from_bytes(file.read(2), 'big')
    print(f)
    g = int.from_bytes(file.read(4), 'big')
    print(g)
    h = int.from_bytes(file.read(4), 'big')
    print(h)
    i = int.from_bytes(file.read(4), 'big')
    print(i)

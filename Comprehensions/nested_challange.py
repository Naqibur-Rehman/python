for i in range(1, 11):
    for j in range(1, 11):
        print(i, i * j)


times = [(i, i * j) for i in range(1, 11) for j in range(1, 11)]
print(times)

for x, y in [(i, i * j) for i in range(1, 11) for j in range(1, 11)]:
    print(x, y)

# for x, y in times:
#     print(x, y)

times2 = [[(i, i * j) for i in range(1, 11)] for j in range(1, 11)]
print(times2)

times3 = [(j, i * j) for j in range(1, 11) for i in range(1, 11)]
print(times3)

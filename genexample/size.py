import sys


def my_range(n: int):
    print("my_range starts")
    start = 0
    while start < n:
        print("my_range id returning {} ".format(start))
        yield start
        start += 1


# big_range = range(15)
big_range = my_range(5)
# _ = input("line15")

print(next(big_range))
print("big_range is {} bytes".format(sys.getsizeof(big_range)))

# create a list containing all the values in big_range
big_list = []
# _ = input("line22")
for val in big_range:
    # _ = input("line24 - inside for loop")
    big_list.append(val)

print("big_list is {} bytes".format(sys.getsizeof(big_list)))
print(big_range)
print(big_list)

print("looping again or not")
for i in my_range(5):
    print("i is {}".format(i))

# def average(*args):
#     print(type(args))
#     print("args is {}".format(args))
#     print("*args is : ", *args)
#     mean = 0
#     for arg in args:
#         mean += arg
#     return mean / len(args)
#
#
# print(average(1, 2, 3, 4))

#  ================  To build a tuple ====================
# def build_tuple(*args):
#     return args
#
#
# message_tuple = build_tuple("naqeeb", "hello", 'kala', 'rehman')
# print(type(message_tuple))
# print(message_tuple)
#
# ===================  it can unpack list as well as tuple=================
# words = ['he', 'is', 'ghost']
# print(*words)


# =============== print arguments passed in reverse order =================
# def print_backwards(*args, end=' ', **kwargs):
#     print(kwargs)
#     for words in args[::-1]:
#         print(words[::-1], end=end, **kwargs)

def print_backwards(*args, end=' ', **kwargs):
    end_character = kwargs.pop('end', '\n')
    sep_character = kwargs.pop('sep', ' ')
    for words in args[:0:-1]:   # change the range
        print(words[::-1], end=sep_character, **kwargs)
    print(args[0][::-1], end=sep_character, **kwargs)  # and prints the first separately
    # print(end=end_character)  # which means we don't need this line


def backwards_print(*args, **kwargs):
    sep_character = kwargs.pop('sep', ' ')
    print(sep_character.join(word[::-1] for word in args[::-1]), **kwargs)


with open("backwards.txt", 'w') as backwards:
    print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='\n')
    print("another string")

print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print("=" * 20)
print_backwards("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print("=" * 20)
backwards_print("hello", "planet", "earth", "take", "me", "to", "your", "leader", end='', sep='\n**\n')
print("=" * 20)

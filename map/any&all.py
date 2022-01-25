entries = [1, 2, 3, 4]

print("all: {}".format(all(entries)))
print("any: {}".format(any(entries)))

print("Iterable with a 'false' value")
entries_with_zero = [1, 2, 0, 4, 5]
print("all: {}".format(all(entries_with_zero)))
print("any: {}".format(any(entries_with_zero)))

print()
print("Values interpreted as 'false' in python")
print("""False: \t\t\t{0}
None: \t\t\t{1}
0: \t\t\t\t{2}
0.0:  \t\t\t{3}
empty list []:  {4}
empty tuple (): {5}
empty string '': {6}
empty string "": {7}
empty mapping {{}}: {8}
""".format(False, bool(None), bool(0), bool(0.0), bool([]), bool(()), bool(''), bool(""), bool({})))

print("=" * 40)
name = "Naqeen"
if name:
    print("Hello {}".format(name))
else:
    print("Welcome, person with no name")

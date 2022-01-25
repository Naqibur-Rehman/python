import shelve

# with shelve.open("ShelfTest") as fruit:
fruit = shelve.open("ShelfTest")
# fruit['orange'] = "a sweet, orange, citrus fruit"
# fruit['lemon'] = "a sour, yellow, citrus fruit"
# fruit['apple'] = "good for making cider"
# fruit['grapes'] = "a small, sweet fruit grows in bunches"
# fruit['lime'] = "a sour, green, citrus fruit"

# print(fruit['lemon'])
# print(fruit['grapes'])
#
# fruit['lemon'] = "great with tequila"   # We can update like dictionary
#
# print(fruit['lemon'])
#
# for snack in fruit:
#     print(snack + " : " + fruit[snack])
#
# while True:
#     dict_key = input("Please enter a fruit : ")
#     if dict_key == "quit":
#         break
#
#     description = fruit.get(dict_key, "We don't have " + dict_key)    # To avoid error if a key is not present
#     print(description)

# sorted_key = list(fruit.keys())
# sorted_key.sort()
# for f in sorted_key:
#     print(f + " - " + fruit[f])

for v in fruit.values():
    print(v)

print(fruit.values())

for i in fruit.items():
    print(i)

print(fruit.items())

fruit.close()      # We need to close file in this mode no need to close with with method

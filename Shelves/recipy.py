import shelve

# blt = ["bacon", "lettuce", "tomato", "bread"]
# beans_on_toast = ["beans", "bread"]
# scrambled_egg = ["eggs", "milk","butter"]
soup = ["tin of soup"]
# pasta = ["pasta", "cheese"]

with shelve.open("recipes", writeback=True) as recipes:
    # recipes["blt"] = blt
    # recipes["beans_on_toast"] = beans_on_toast
    # recipes["scrambled_egg"] = scrambled_egg
    # recipes["soup"] = soup
    # recipes["pasta"] = pasta

    # recipes["blt"].append("butter")     # no appending takes place
    # recipes["pasta"].append("tomato")

    # temp_list = recipes["blt"]
    # temp_list.append("butter")
    # recipes["blt"] = temp_list

    # temp_list2 = recipes["pasta"]
    # temp_list2.append("tomato")
    # recipes["pasta"] = temp_list2

    recipes["soup"].append("croutons")   # writeback use
    recipes["soup"] = soup
    recipes.sync()            # sync clears the cache
    soup.append("cream")

    for snack in recipes:
        print(snack, recipes[snack])


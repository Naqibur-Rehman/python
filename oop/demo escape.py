a_string = "This is\na string split\t\tand tabbed"
print(a_string)

raw_string = r"This is\na string split\t\tand tabbed"
print(raw_string)

b_string = "This is" + chr(13) + "a string split" + chr(13) + chr(13) + "and tabbed"
print(b_string)

backslash_string = "This is a backslash \followed by some text"
print(backslash_string)

backslash_string = "This is a backslash \\followed by some text"
print(backslash_string)

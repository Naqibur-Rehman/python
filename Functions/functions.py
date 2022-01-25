def python_food():
    width = 170
    text = "spam and eggs"
    left_margin = (width - len(text)) // 2
    print(" " * left_margin, text)


def centre_text(*args, sep=" ", end='\n', file=None, flush=False):
    text = ""
    for arg in args:
        text += str(arg) + sep
        # text += str(arg) + " "
    left_margin = (170 - len(text)) // 2
    print(" " * left_margin, text, end=end, file=file, flush=flush)


# call the function
centre_text(12)
centre_text("spam and eggs")
centre_text("spam, spam and eggs")
centre_text("spam, spam, spam and spam")
centre_text("spam", 6, "eggs", 2, "tomatoes", sep=":")

# for saving into file
with open("centered", mode='w') as centered_file:
    centre_text(12, file=centered_file)
    centre_text("spam and eggs", file=centered_file)
    centre_text("spam, spam and eggs", file=centered_file)
    centre_text("spam, spam, spam and spam", file=centered_file)
    centre_text("spam", 6, "eggs", 2, "tomatoes", sep=":", file=centered_file)
